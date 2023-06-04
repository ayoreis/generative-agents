from typing import NamedTuple
from datetime import datetime
import re

from chat_gpt import ChatGPT
from memory_stream import MemoryStream
from memory import Memory
from completions import complete
from embeddings import embedding
from maths import SECONDS_IN_HOUR, min_max_scale, cosine_similarity
from reflections import Reflection

DIGIT = re.compile("\d")
# TODO conform to https://spec.commonmark.org/0.30/#list-items
LIST_ITEM = re.compile("\d[.)] (?P<high_level_question>.+?)(?:\n|$)")
CITATIONS = re.compile(" \((\d)(?P<citation>, \d)*\)$")

NEWLINE = "\n"


def parse_list_items(string: str):
    return [
        list_item.group("high_level_question")
        for list_item in re.finditer(LIST_ITEM, string)
    ]


class Score(NamedTuple):
    score: float
    memory: Memory


class Agent:
    MEMORY_SEPARATOR = "; "
    DECAY_FACTOR = 0.99

    ALPHA = 1

    ALPHA_RECENCY = ALPHA
    APLHA_IMPORTANCE = ALPHA
    ALPHA_RELEVANCE = ALPHA

    def __init__(self, initial_memories_string: str):
        # TODO make dynamic
        self.name = "Josh"

        self.chat_gpt = ChatGPT()
        self.memory_stream = MemoryStream()

        for memory in initial_memories_string.split(self.MEMORY_SEPARATOR):
            self.create_memory(memory)

    def calculate_importance(self, memory_description: str):
        prompt = f"""On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.
Memory: {memory_description}
Rating: <fill in>"""

        while True:
            try:
                # NOTE not using `self.chat_gpt.message` because when in answered "I'm an AI assistant", it'd gets stuck on that for the next tries, should we? If yes, move this to a standalone function/`Memory`?
                # Something like `ChatGPT.back_up_conversation`?
                # TODO limit response length
                response = complete(prompt)

                # TODO Only find nessesary amount (2) using `re.finditer`
                matches = re.findall(DIGIT, response)

                if len(matches) != 1:
                    raise

                importance = float(matches[0])

                return importance
            except:
                print(response)

    def create_memory(self, description: str):
        importance = self.calculate_importance(description)
        memory = Memory(description, importance)
        self.memory_stream.stream.append(memory)

    def retrieve_memories(self, agents_current_situation: str):
        scores: list[Score] = []

        for memory in self.memory_stream.stream:
            now = datetime.now()
            hours_since_last_retrieval = (
                now - memory.most_recent_access_timestamp
            ).total_seconds() / SECONDS_IN_HOUR

            recency = min_max_scale(
                self.DECAY_FACTOR**hours_since_last_retrieval, 0, 1
            )
            importance = min_max_scale(memory.importance, 0, 10)
            relevance = min_max_scale(
                cosine_similarity(
                    memory.embedding, embedding(agents_current_situation)
                ),
                -1,
                1,
            )

            score = (
                self.ALPHA_RECENCY * recency
                + self.APLHA_IMPORTANCE * importance
                + self.ALPHA_RELEVANCE * relevance
            )

            scores.append(Score(score, memory))

        scores.sort(key=lambda e: e.score, reverse=True)

        return scores

    def observe(self, observation: str):
        self.create_memory(observation)

    def reflect(self):
        prompt = f"""{self.MEMORY_SEPARATOR.join(memory.description for memory in self.memory_stream.stream[-100:])}

        Given only the information above, what are 3 most salient high-level questions we can answer about the subjects in the statements?
        """

        high_level_questions = parse_list_items(self.chat_gpt.message(prompt))

        for high_level_question in high_level_questions:
            scores = self.retrieve_memories(high_level_question)[:3]

            for score in scores:
                score.memory.access()

            memories = (score.memory for score in scores)

            # TODO "example format" does not work, need better wording
            prompt = f"""Statements about {self.name}
{NEWLINE.join(f'{index}. {memory}' for index, memory in enumerate(memories, 1))}
What 5 high-level insights can you infer from the above statements? (example format: insight (because of 1, 5, 3))"""

            reflection_descriptions = parse_list_items(self.chat_gpt.message(prompt))

            for description in reflection_descriptions:
                importance = self.calculate_importance(description)

                # citations = re.search(CITATIONS, description).groups()
                # description = re.sub(CITATIONS, "", description)

                reflection = Reflection(description, importance, memories)

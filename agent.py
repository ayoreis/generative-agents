from typing import NamedTuple
from datetime import datetime
from re import compile, MULTILINE

from chat_gpt import ChatGPT
from memory_stream import MemoryStream
from memory import Memory
from embeddings import embedding
from maths import SECONDS_IN_HOUR, min_max_scale, cosine_similarity
from reflections import Reflection


LIST_ITEM = compile("^ {0,3}(?:[-+*]|[0-9]{1,9}[.)])(?: {1,4}|\t)(.*?)$", MULTILINE)

NEWLINE = "\n"


def parse_list_items(string: str):
    return (item.group(1) for item in LIST_ITEM.finditer(string))


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

    def __init__(self, description: str):
        # TODO make dynamic
        self.name = "Josh"

        self.chat_gpt = ChatGPT()
        self.memory_stream = MemoryStream()

        for memory_description in description.split(self.MEMORY_SEPARATOR):
            self.memory_stream.stream.append(Memory(memory_description))

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
        self.memory_stream.stream.append(Memory(observation))

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

            # TODO "example format" doesn't work, need better wording
            prompt = f"""Statements about {self.name}
{NEWLINE.join(f'{index}. {memory}' for index, memory in enumerate(memories, 1))}
What 5 high-level insights can you infer from the above statements? (example format: insight (because of 1, 5, 3))"""

            reflection_descriptions = parse_list_items(self.chat_gpt.message(prompt))

            for description in reflection_descriptions:
                reflection = Reflection(description, tuple(memories))

                self.memory_stream.stream.append(reflection)

from re import compile, MULTILINE

from chat_gpt import ChatGPT
from memory_stream import MemoryStream
from memory import Memory
from reflections import Reflection
from completions import complete
from plan import Plan
from nodes import World, Area, Object
from maths import Point

LIST_ITEM = compile("^ {0,3}(?:[-+*]|[0-9]{1,9}[.)])(?: {1,4}|\t)(.*?)$", MULTILINE)

NEWLINE = "\n"


def parse_list_items(string: str):
    return (item.group(1) for item in LIST_ITEM.finditer(string))


class Agent:
    MEMORY_SEPARATOR = "; "

    DECAY_FACTOR = 0.99

    ALPHA = 1
    ALPHA_RECENCY = ALPHA
    APLHA_IMPORTANCE = ALPHA
    ALPHA_RELEVANCE = ALPHA

    def __init__(
        self,
        name: str,
        age: float,
        traits: str,
        description: str,
        environment: World,
        # TODO should this be in Sandbox?
        current_location: Area,
        description_of_current_action: str,
        interacting_sandbox_object: Object,
    ):
        self.name = name
        self.age = age
        self.traits = traits

        self.memory_stream = MemoryStream()

        for memory_description in description.split(self.MEMORY_SEPARATOR):
            self.memory_stream.stream.append(Memory(memory_description))

        self.current_location = current_location
        self.description_of_current_action = description_of_current_action
        self.interacting_sandbox_object = interacting_sandbox_object

    def observe(self, observation: str):
        self.memory_stream.stream.append(Memory(observation))

    #     def reflect(self):
    #         prompt = f"""{self.MEMORY_SEPARATOR.join(memory.description for memory in self.memory_stream.stream[-100:])}

    #         Given only the information above, what are 3 most salient high-level questions we can answer about the subjects in the statements?
    #         """

    #         high_level_questions = parse_list_items(self.chat_gpt.message(prompt))

    #         for high_level_question in high_level_questions:
    #             scores = self.memory_stream.retrieve_memories(high_level_question)[:3]

    #             for score in scores:
    #                 score.memory.access()

    #             memories = (score.memory for score in scores)

    #             # TODO "example format" doesn't work, need better wording
    #             prompt = f"""Statements about {self.name}
    # {NEWLINE.join(f'{index}. {memory}' for index, memory in enumerate(memories, 1))}
    # What 5 high-level insights can you infer from the above statements? (example format: insight (because of 1, 5, 3))"""

    #             reflection_descriptions = parse_list_items(self.chat_gpt.message(prompt))

    #             for description in reflection_descriptions:
    #                 reflection = Reflection(description, tuple(memories))

    #                 self.memory_stream.stream.append(reflection)

    #     def summary_description(self):
    #         core_characteristics_memories = self.memory_stream.retrieve_memories(
    #             f"{self.name}’s core characteristics"
    #         )[:10]

    #         core_characteristics = complete(
    #             f"""How would one describe {self.name}’s core characteristics given the following statements?
    # - {f'{NEWLINE}- '.join(str(score.memory) for score in core_characteristics_memories)}"""
    #         )

    #     current_situation = "doing somethis"

    #     def plan(self):
    #         intial_plan_prompt = """Name: Eddy Lin (age: 19)
    # Innate traits: friendly, outgoing, hospitable
    # Eddy Lin is a student at Oak Hill College studying music theory and composition. He loves to explore different musical styles and is always looking for ways to expand his knowledge. Eddy Lin is working on a composition project for his college class. He is also taking classes to learn more about music theory. Eddy Lin is excited about the new composition he is working on but he wants to dedicate more hours in the day to work on it in the coming days
    # On Tuesday February 12, Eddy 1) woke up and completed the morning routine at 7:00 am, [. . . ] 6) got ready to sleep around 10 pm.
    # Today is Wednesday February 13. Here is Eddy’s
    # plan today in broad strokes: 1)"""

    #         initial_plan = complete(intial_plan_prompt)

    #         plan = Plan(initial_plan, "...", "6am", "12h")

    #     def react(self):
    #         p = f"""[Agent’s Summary Description]
    # It is February 13, 2023, 4:56 pm.
    # {self.name}’s status: John is back home early from
    # work.
    # Observation: ...
    # Summary of relevant context from {self.name}’s memory:
    # What is [observer]’s relationship
    # with the [observed entity]? [Observed entity] is [action status
    # of the observed entity]”
    # Should {self.name} react to the observation, and if so,
    # what would be an appropriate reaction?"""

    def __str__(self):
        return f"{self.name} is {self.description_of_current_action}"

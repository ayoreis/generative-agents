from time import time
from itertools import chain

from agent import Agent
from nodes import World, Object
from maths import center, distance, Rectangle


class Sandbox:
    """5"""

    TICKS_PER_SECOND = 1
    SECONDS_PER_TICK = 1 / TICKS_PER_SECOND
    TIME_RATIO = 60

    VISUAL_RANGE = 10

    def __init__(self, agents: tuple[Agent], world: World):
        self.agents = agents
        self.world = world

        self.start_time = time()
        self.time = self.start_time

    def tick(self):
        for agent in self.agents:
            for agent_or_object in self.sight(agent):
                agent.observe(str(agent_or_object))

        # TODO exclude reflections and plans
        # if (
        #     sum(
        #         [
        #             event.importance
        #             for event in agent.memory_stream.stream[EVENTS * -1 :]
        #         ]
        #     )
        #     > THRESHOLD
        # ):
        #     agent.reflect()

        #     agent.plan()

        # if agent.should_react():
        #     agent.react()

        self.time += self.SECONDS_PER_TICK * self.TIME_RATIO

    def in_visual_range(self, rectangle_a: Rectangle, rectangle_b: Rectangle):
        return distance(center(rectangle_a), center(rectangle_b)) < self.VISUAL_RANGE

    def sight(self, agent: Agent):
        return chain(
            (
                child
                for child in agent.current_location.children
                if isinstance(child, Object)
                and self.in_visual_range(
                    agent.current_location.rectangle, child.rectangle
                )
            ),
            (
                other_agent
                for other_agent in self.agents
                if not other_agent == agent
                and self.in_visual_range(
                    agent.current_location.rectangle,
                    other_agent.current_location.rectangle,
                )
            ),
        )

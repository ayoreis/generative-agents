import openai_secrets

from agent import Agent
from nodes import World, Area, Object
from sandbox import Sandbox

table = Object("Table", (2.5, 3, 2, 1), "ocupied by Ayo")
room = Area("Room", (1, 1, 5, 5), (table,))

agents = (
    Agent(
        name="Ayo Reis",
        age=15,
        traits="Shy, curious",
        description="Table is empty",
        environment=None,
        current_location=room,
        description_of_current_action="Sitting at a table",
        interacting_sandbox_object=table,
    ),
)

place = World((room,))
sandbox = Sandbox(agents, place)

sandbox.tick()

print(agents[0].memory_stream.stream)

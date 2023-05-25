from memory_stream import MemoryStream
from memory import Memory

class Agent:
    memory_stream = MemoryStream()

    def __init__(self, initial_memories: str):
        initial_memories_list = map(Memory, initial_memories.split('; '))

        self.memory_stream.stream.extend(initial_memories_list)

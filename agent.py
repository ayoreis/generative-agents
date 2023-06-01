from datetime import datetime

from chat_gpt import ChatGPT
from memory_stream import MemoryStream
from memory import Memory
from embeddings import embedding
from maths import SECONDS_IN_HOUR, min_max_scale, cosine_similarity

class Agent:
    MEMORY_SEPARATOR = '; '
    DECAY_FACTOR = 0.99

    ALPHA = 1

    ALPHA_RECENCY = ALPHA
    APLHA_IMPORTANCE = ALPHA
    ALPHA_RELEVANCE = ALPHA

    def __init__(self, initial_memories_string: str):
        self.chat_gpt = ChatGPT()
        self.memory_stream = MemoryStream()

        for memory in initial_memories_string.split(self.MEMORY_SEPARATOR):
            self.create_memory(memory)

    def create_memory(self, natural_language_description: str):
        importance = float(self.chat_gpt.message(f'''On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.
Memory: {natural_language_description}
Rating: <fill in>'''))

        memory = Memory(natural_language_description, importance)

        self.memory_stream.stream.append(memory)

    def retrieve_memories(self, agents_current_situation: str):
        print(f'{agents_current_situation}\n')

        for memory in self.memory_stream.stream:
            now = datetime.now()
            hours_since_last_retrieval = (now - memory.most_recent_access_timestamp).total_seconds() / SECONDS_IN_HOUR

            recency = min_max_scale(self.DECAY_FACTOR ** hours_since_last_retrieval, 0, 1)
            importance = min_max_scale(memory.importance, 0, 10)
            relevance = min_max_scale(cosine_similarity(memory.embedding, embedding(agents_current_situation)), -1, 1)

            score = self.ALPHA_RECENCY * recency + self.APLHA_IMPORTANCE * importance + self.ALPHA_RELEVANCE * relevance

            print(f'{memory.natural_language_description}: {score}')

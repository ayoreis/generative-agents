from memory import Memory
from embeddings import embedding
from maths import SECONDS_IN_HOUR, min_max_scale, cosine_similarity
from datetime import datetime
from typing import NamedTuple


class Score(NamedTuple):
    score: float
    memory: Memory


class MemoryStream:
    """4.1"""

    def __init__(self):
        self.stream: list[Memory] = []

    def retrieve_memories(self, agents_current_situation: str):
        def sort(self, memory: Memory):
            hours_since_last_retrieval = (
                datetime.now() - memory.most_recent_access_timestamp
            ).total_seconds() / SECONDS_IN_HOUR

            recency = self.DECAY_FACTOR**hours_since_last_retrieval
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

            return Score(score, memory)

        return sorted(self.stream, sort, True)

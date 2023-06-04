from datetime import datetime

from embeddings import embedding


class Memory:
    """4.1"""

    def __init__(self, description: str, importance: int):
        now = datetime.now()

        self.description = description
        self.creation_timestamp = now
        self.most_recent_access_timestamp = now

        self.importance = importance
        self.embedding = embedding(description)

    def __repr__(self):
        return self.description

    def access(self):
        self.most_recent_access_timestamp = datetime.now()

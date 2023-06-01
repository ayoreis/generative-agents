import datetime

from embeddings import embedding

class Memory:
    def __init__(self, natural_language_description: str, importance: int):
        now = datetime.datetime.now()

        self.natural_language_description = natural_language_description
        self.creation_timestamp = now
        self.most_recent_access_timestamp = now

        self.importance = importance
        self.embedding = embedding(natural_language_description)

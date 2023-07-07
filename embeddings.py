from openai import Embedding

MODEL = "text-embedding-ada-002"


def embedding(text: str):
    return Embedding.create(model=MODEL, input=text).data[0].embedding

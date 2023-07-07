from re import compile
from datetime import datetime

from embeddings import embedding
from completions import complete

DIGIT = compile("\d+")


class Memory:
    """4.1"""

    #     IMPORTANCE_PROMPT = """On the scale of 1 to 10, where 1 is purely mundane (e.g., brushing teeth, making bed) and 10 is extremely poignant (e.g., a break up, college acceptance), rate the likely poignancy of the following piece of memory.
    # Memory: {}
    # Rating: <fill in>"""

    def __init__(self, description: str):
        now = datetime.now()

        self.description = description
        self.creation_timestamp = now
        self.most_recent_access_timestamp = now

        self.importance = None
        self.embedding = embedding(description)

        # prompt = self.IMPORTANCE_PROMPT.format(description)

        # while self.importance == None:
        #     try:
        #         completion = complete(prompt, 2)

        #         matches = DIGIT.findall(completion)

        #         if len(matches) != 1:
        #             raise

        #         self.importance = float(matches[0])
        #     except:
        #         # For debugging
        #         print(completion)

    def __repr__(self):
        return self.description

    def access(self):
        self.most_recent_access_timestamp = datetime.now()

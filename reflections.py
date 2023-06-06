from memory import Memory


class Reflection(Memory):
    """4.2"""

    def __init__(self, description: str, citations: tuple[Memory]):
        super().__init__(description)

        self.citations = citations

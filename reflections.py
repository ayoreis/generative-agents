from memory import Memory


class Reflection(Memory):
    """4.2"""

    def __init__(self, description: str, importance: int, citations: tuple[Memory]):
        super().__init__(description, importance)

        self.citations = citations

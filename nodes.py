from __future__ import annotations

from maths import Rectangle


class Area:
    """Figure 2"""

    def __init__(
        self,
        name: str,
        rectangle: Rectangle,
        children: tuple[Area | Object, ...],
    ):
        self.name = name
        self.rectangle = rectangle
        self.children = children


class World:
    """Figure 2"""

    def __init__(self, children=tuple[Area, ...]):
        self.children = children


class Object:
    """Figure 2"""

    def __init__(self, name: str, rectangle: Rectangle, state: str):
        self.name = name
        self.rectangle = rectangle
        self.state = state

    def __str__(self):
        return f"{self.name} is {self.state}"

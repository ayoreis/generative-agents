from math import sqrt, hypot

Number = int | float
Vector = tuple[Number, ...]
"""https://en.wikipedia.org/wiki/Coordinate_vector"""
Point = tuple[Number, Number]
"""x, y"""
Rectangle = tuple[Number, Number, Number, Number]
"""x, y, width, height"""

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

SECONDS_IN_HOUR = MINUTES_IN_HOUR * SECONDS_IN_MINUTE


def min_max_scale(x: Number, min_x: Number, max_x: Number):
    """https://en.wikipedia.org/wiki/Feature_scaling#Rescaling_(min-max_normalization)"""
    return (x - min_x) / (max_x - min_x)


def dot_product(a: Vector, b: Vector):
    """https://en.wikipedia.org/wiki/Dot_product"""
    return sum(i * j for i, j in zip(a, b))


def cosine_similarity(a: Vector, b: Vector):
    """https://en.wikipedia.org/wiki/Cosine_similarity"""
    return dot_product(a, b) / (
        sqrt(sum(i**2 for i in a)) * sqrt(sum(i**2 for i in b))
    )


# def average(a: Vector) -> Number:
#     """https://en.wikipedia.org/wiki/Average"""
#     return sum(a) / len(a)


def center(rectangle: Rectangle) -> Point:
    return (
        rectangle[0] + rectangle[2] / 2,
        rectangle[1] + rectangle[3] / 2,
    )


def distance(a: Point, b: Point) -> float:
    return hypot(a[0] - b[0], a[1] - b[1])

from math import sqrt

Number = int | float
Vector = tuple[Number] | list[Number]

SECONDS_IN_MINUTE = 60
MINUTES_IN_HOUR = 60

SECONDS_IN_HOUR = MINUTES_IN_HOUR * SECONDS_IN_MINUTE

def min_max_scale(x: Number, min: Number, max: Number):
    return (x - min) / (max - min)

def dot_product(a: Vector, b: Vector):
    return sum((i * j for i, j in zip(a, b)))

def square_sum_sqrt(a: Vector):
    return sqrt(sum((i ** 2 for i in a)))

def cosine_similarity(a: Vector, b: Vector):
    return dot_product(a, b) / (square_sum_sqrt(a) * square_sum_sqrt(b))

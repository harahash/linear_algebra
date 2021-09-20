import math
from typing import List

Vector = List[float]


def add(a: Vector, b: Vector) -> Vector:
    """Adds corresponding elements"""

    assert len(a) == len(b), 'vectors must have the same length'
    return [a_i + b_i for a_i, b_i in zip(a, b)]


assert add([1, 2, 3], [4, 5, 6]) == [5, 7, 9]


def substract(a: Vector, b: Vector) -> Vector:
    """Subtracts corresponding elements"""

    assert len(a) == len(b), 'vectors must have the same length'
    return [a_i - b_i for a_i, b_i in zip(a, b)]


assert substract([5, 7, 9], [4, 5, 6]) == [1, 2, 3]


def vector_sum(vectors: List[Vector]) -> Vector:
    """Sums all corresponding elements"""
    assert vectors, 'there is no vectors'
    num_elements = len(vectors[0])
    assert all(len(
        v) == num_elements for v in vectors), 'there is vector(s) with different size(s)'
    return [sum(vector[i] for vector in vectors)
            for i in range(num_elements)]


assert vector_sum([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]) == [25, 30]


def vector_scalar_multiply(s: float, a: Vector) -> Vector:
    return [s * a_i for a_i in a]


assert vector_scalar_multiply(3, [2, 4, 6]) == [6, 12, 18]


def vector_mean(vectors: List[Vector]) -> Vector:
    n = len(vectors)
    return vector_scalar_multiply(1/n, vector_sum(vectors))


assert vector_mean([[1, 2], [3, 4], [5, 6]]) == [3, 4]


def scalar_multiply(a: Vector, b: Vector) -> float:
    assert len(a) == len(b), 'vectors must have the same length'
    return sum(a_i * b_i for a_i, b_i in zip(a, b))


assert scalar_multiply([1, 3, 5], [2, 4, 6]) == 44


def sum_of_squares(a: Vector) -> float:
    return scalar_multiply(a, a)


assert sum_of_squares([1, 2, 3]) == 14


def magnitude(a: Vector) -> float:
    """length of vector a"""
    return math.sqrt(sum_of_squares(a))


assert magnitude([3, 4]) == 5


def squared_distance(a: Vector, b: Vector) -> float:
    """Computes (a_1 - a_1) ** 2 + ... + (a_n - a_n) ** 2"""
    return sum_of_squares(substract(a, b))


def distance(a: Vector, b: Vector) -> float:
    """Computes distance between a and b"""
    return magnitude(substract(a, b))

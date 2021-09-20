from typing import List, Tuple, Callable


Matrix = List[List[float]]
Vector = List[float]

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 2],
     [3, 4],
     [5, 6]]


def shape(A: Matrix) -> Tuple[int, int]:
    """returns number of cols and rows in matrix A"""
    num_rows = len(A)
    num_cols = len(A[0]) if A else 0
    return num_rows, num_cols


assert shape([[1, 2, 3], [4, 5, 6]]) == (2, 3)  # 2 rows, 3 cols


def get_row(A: Matrix, i: int) -> Vector:
    """returns i-row of matrix A"""
    return A[i]


def get_column(A: Matrix, j: int) -> Vector:
    """returns j-col of matrix A"""
    return [A_i[j] for A_i in A]


def make_matrix(num_rows: int,
                num_cols: int,
                entry_fn: Callable[[int, int], float]) -> Matrix:
    """creates matrix num_rows x num_cols"""
    return [[entry_fn(i, j)
             for j in range(num_cols)]  # [entry_fn(i, 0), ...]
            for i in range(num_rows)]


def identity_matrix(n: int) -> Matrix:
    """returns identity matrix"""
    return make_matrix(n, n, lambda i, j: 1 if i == j else 0)


assert identity_matrix(5) == [[1, 0, 0, 0, 0],
                              [0, 1, 0, 0, 0],
                              [0, 0, 1, 0, 0],
                              [0, 0, 0, 1, 0],
                              [0, 0, 0, 0, 1]]


friendships = [[0, 1, 1, 0, 0, 0, 0, 0, 0, 0],  # user 0
               [1, 0, 1, 1, 0, 0, 0, 0, 0, 0],  # 1
               [1, 1, 0, 1, 0, 0, 0, 0, 0, 0],  # 2
               [0, 1, 1, 0, 1, 0, 0, 0, 0, 0],  # 3
               [0, 0, 0, 1, 0, 1, 0, 0, 0, 0],  # 4
               [0, 0, 0, 0, 1, 0, 1, 1, 0, 0],  # 5
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 6
               [0, 0, 0, 0, 0, 1, 0, 0, 1, 0],  # 7
               [0, 0, 0, 0, 0, 0, 1, 1, 0, 1],  # 8
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  # 9

assert friendships[3][2] == 1, "3 and 2 are friends"
assert friendships[6][7] == 0, "6 and 7 are not friends"


friends_of_one = [i
                  for i, is_friend in enumerate(friendships[1])
                  if is_friend]

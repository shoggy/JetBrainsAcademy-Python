from io import StringIO

import numpy as np
from numpy import linalg as la


def print_matrix(matrix: np.ndarray):
    s = StringIO()
    np.savetxt(s, matrix, fmt="%.3f")
    print(s.getvalue())


def calculate_pagerank(matrix: np.ndarray, damp_fact=1., prec=0.01) -> np.ndarray:
    n = np.size(matrix, 0)
    m = damp_fact * matrix + (1 - damp_fact) / n * np.ones((n, n))
    r = 100 * np.ones(n) / n

    while True:
        r_prev = r
        r = m @ r
        if la.norm(r_prev - r) <= prec:
            break
    return r


L = np.array([
    [0,   1/2, 1/3, 0, 0,   0],
    [1/3, 0,   0,   0, 1/2, 0],
    [1/3, 1/2, 0,   1, 0,   1/2],
    [1/3, 0,   1/3, 0, 1/2, 1/2],
    [0,   0,   0,   0, 0,   0],
    [0,   0,   1/3, 0, 0,   0]
])

L2 = np.array([
    [0,   1/2, 1/3, 0, 0,   0,   0],
    [1/3, 0,   0,   0, 1/2, 0, 0],
    [1/3, 1/2, 0,   1, 0,   1/3,   0],
    [1/3, 0,   1/3, 0, 1/2, 1/3, 0],
    [0,   0,   0,   0, 0,   0,   0],
    [0,   0,   1/3, 0, 0,   0,   0],
    [0,   0,   0,   0, 0,   1/3, 1]
])

print_matrix(L2)
res = calculate_pagerank(L2)
print_matrix(res)
res = calculate_pagerank(L2, damp_fact=0.5)
print_matrix(res)

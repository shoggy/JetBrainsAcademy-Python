from io import StringIO

import numpy as np
from numpy import linalg as la


def print_matrix(matrix: np.ndarray):
    s = StringIO()
    np.savetxt(s, matrix, fmt="%.3f")
    print(s.getvalue())


def pagerank(matrix: np.ndarray, d=1., prec=0.01) -> np.ndarray:
    n = np.size(matrix, 0)
    m = d * matrix + (1 - d) / n * np.ones((n, n))
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

input_line = input().split()
n = int(input_line[0])
d = float(input_line[1])
L3 = []
for _ in range(n):
    L3.append([float(x) for x in input().split()])
L3 = np.array(L3)
print_matrix(pagerank(L3, d=d))

from io import StringIO
import numpy as np
from numpy import linalg as la


def print_matrix(matrix: np.ndarray):
    s = StringIO()
    np.savetxt(s, matrix, fmt="%.3f")
    print(s.getvalue())


def normalize_vector(vector: np.ndarray) -> np.ndarray:
    norm_value = 100 / sum(vector).real
    normalized_vector = np.real(vector * norm_value)
    return normalized_vector


L = np.array([
    [0,   1/2, 1/3, 0, 0,   0],
    [1/3, 0,   0,   0, 1/2, 0],
    [1/3, 1/2, 0,   1, 0,   1/2],
    [1/3, 0,   1/3, 0, 1/2, 1/2],
    [0,   0,   0,   0, 0,   0],
    [0,   0,   1/3, 0, 0,   0]
])

print_matrix(L)

e_vals, e_vecs = la.eig(L)
vec = np.transpose(e_vecs)[0]
norm_vec = normalize_vector(vec)
print_matrix(norm_vec)

import operator
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


def query(sites: list, ranks: np.ndarray, query: str) -> list:
    top_res = None
    ranks = ranks.tolist()
    if query in sites:
        idx = sites.index(query)
        sites.pop(idx)
        ranks.pop(idx)
        top_res = (query, )
    site_list = list(zip(sites, ranks))
    site_list = sorted(site_list, key=operator.itemgetter(1, 0), reverse=True)
    if top_res is not None:
        site_list.insert(0, top_res)
    return site_list[:5]


n = int(input())
d = 0.5
sites = input().split()[:n]
L3 = []
for _ in range(n):
    L3.append([float(x) for x in input().split()])
L3 = np.array(L3)
ranks = pagerank(L3, d=d)
query_str = input()

for x in query(sites, ranks, query_str):
    print(x[0])

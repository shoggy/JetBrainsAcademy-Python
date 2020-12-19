import numpy as np

a = int(input())
b = int(input())
c = int(input())
d = int(input())

arr = np.array([[a, b], [c, d]])
v, w = np.linalg.eig(arr)
print(v)

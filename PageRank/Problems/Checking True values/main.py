import numpy as np

a = int(input())
b = int(input())
c = int(input())

a1 = np.array([a, b, c])
print(np.all(a1 > 15))

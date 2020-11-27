import numpy as np

a = int(input())
b = int(input())
c = int(input())

print(np.linspace(a, b, num=c)[-2])

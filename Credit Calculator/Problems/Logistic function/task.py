import math

x = int(input())
v = 1 / (1 + math.exp(-x))
print(round(v, 2))

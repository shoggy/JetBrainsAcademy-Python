import math

a = int(input())
b = int(input())
res = None
if b < 0 or b == 0 or b == 1:
    res = math.log(a)
else:
    res = math.log(a, b)
print(round(res, 2))

from math import sqrt

a = int(input())
area = 2 * sqrt(3) * a * a
volume = sqrt(2) * a * a * a / 3
print(f"{area:.2f} {volume:.2f}")

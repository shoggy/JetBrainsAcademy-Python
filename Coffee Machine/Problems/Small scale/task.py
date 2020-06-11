m = float(input())
s = input()
while s != '.':
    m = min(m, float(s))
    s = input()
print(m)

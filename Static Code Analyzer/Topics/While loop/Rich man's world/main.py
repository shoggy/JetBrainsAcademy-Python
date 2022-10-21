n = int(input())
c = 0
while n < 700_000:
    n *= 1.071
    c += 1
print(c)

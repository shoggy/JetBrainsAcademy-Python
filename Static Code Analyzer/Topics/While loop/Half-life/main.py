n = int(input())
r = int(input())
c = 0
while n > r:
    n //= 2
    c += 1
print(c * 12)

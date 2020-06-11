s = 0
c = 0
while True:
    t = input()
    if t == '.':
        break
    s += int(t)
    c += 1
print(s / c)

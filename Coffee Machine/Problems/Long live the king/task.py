x = int(input())
y = int(input())
c = 0
if x > y:
    x, y = y, x
if x in (1, 8) and y in (1, 8):
    c = 3
elif x in (1, 8) or y in (1, 8):
    c = 5
else:
    c = 8
print(c)

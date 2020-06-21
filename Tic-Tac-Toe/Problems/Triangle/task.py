x = int(input())
y = 2 * x - 1
for i in range(1, x + 1):
    print(('#' * (2 * i - 1)).center(y, ' '))

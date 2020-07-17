n = int(input())


def squares():
    i = 0
    while True:
        i += 1
        yield i * i


# Don't forget to print out the first n numbers one by one here
gen = squares()
for _ in range(n):
    print(next(gen))

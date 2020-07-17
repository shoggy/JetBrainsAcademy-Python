n = int(input())


def even():
    i = 0
    while True:
        yield i + i
        i += 1


# Don't forget to print out the first n numbers one by one here
gen = even()
for _ in range(n):
    print(next(gen))

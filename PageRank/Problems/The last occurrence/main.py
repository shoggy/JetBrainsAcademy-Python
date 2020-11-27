def search(numbers, target):
    i = len(numbers)
    while i > 0:
        i -= 1
        if target == numbers[i]:
            return i
    return -1


num_list = [int(x) for x in input().split()]
t = int(input())
print(search(num_list, t))

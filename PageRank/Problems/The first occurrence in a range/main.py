def search(numbers, target, a, b):
    for i, elem in enumerate(numbers[a:b], a):
        if target == elem:
            return i
    return -1


num_list = [int(i) for i in input().split()]
x = int(input())
(left, right) = (int(i) for i in input().split())

print(search(num_list, x, left, right))

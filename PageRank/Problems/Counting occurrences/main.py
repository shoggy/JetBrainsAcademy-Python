def count(numbers, target):
    cnt = 0
    for elem in numbers:
        if target == elem:
            cnt += 1
    return cnt


num_list = [int(i) for i in input().split()]
a = int(input())
print(count(num_list, a))

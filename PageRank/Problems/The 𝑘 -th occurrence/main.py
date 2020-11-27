def kth(numbers, target, k):
    cnt = 0
    for idx, elem in enumerate(numbers):
        if target == elem:
            cnt += 1
            if cnt == k:
                return idx
    return -1


num_list = [int(i) for i in input().split()]
target_num = int(input())
expected_entry = int(input())
print(kth(num_list, target_num, expected_entry))

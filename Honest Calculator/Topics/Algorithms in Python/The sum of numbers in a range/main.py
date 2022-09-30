def range_sum(number_list, lower, upper):
    acc = 0
    for x in number_list:
        if lower <= x <= upper:
            acc += x
    return acc


numbers = (int(x) for x in input().split())
a, b = (int(x) for x in input().split())
print(range_sum(numbers, a, b))

# the following code creates a list from input, please do not modify it
ints = [int(num) for num in input().split()]

# your solution here
sorted_list = sorted(ints)
print(sorted_list[2], sorted_list[0], sorted_list[1], sep=' ')

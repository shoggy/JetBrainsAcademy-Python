nums = [int(num) for num in list(input())]

# write your code here

result = sorted(nums, key=lambda x: x % 3)
print(result)

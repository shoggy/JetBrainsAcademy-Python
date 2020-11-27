import numpy as np

nums = []
for _ in range(6):
    nums.append(int(input()))

a = np.array([nums[0:2], nums[2:4]])
b = np.array(nums[4:6])

print((a / b).T)

import numpy as np

nums = []
for _ in range(4):
    nums.append(int(input()))

a = np.array([nums[0:2], nums[2:4]])
print(a.T)

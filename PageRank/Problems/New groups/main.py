import itertools

# the list with classes; please, do not modify it
groups = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C']

# your code here
lst = []
n = int(input())
for _ in range(n):
    lst.append(int(input()))
res = dict(itertools.zip_longest(groups, lst))
print(res)

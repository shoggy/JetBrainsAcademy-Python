import collections

shopping_list = input().split()
cnt = collections.Counter(shopping_list)
for k, v in cnt.items():
    print(f"{v} {k}")

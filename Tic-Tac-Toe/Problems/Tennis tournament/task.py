n = int(input())
data = []
for _i in range(n):
    data.append(input().split())
res = [a[0] for a in data if a[1] == "win"]
print(res)
print(len(res))

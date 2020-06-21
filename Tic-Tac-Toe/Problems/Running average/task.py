s = [int(a) for a in input().strip()]
print([(s[i] + s[i + 1]) / 2 for i in range(len(s) - 1)])

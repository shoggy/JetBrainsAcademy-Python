from collections import Counter

stat = Counter(input().split())
print(stat.most_common(1)[0][0])

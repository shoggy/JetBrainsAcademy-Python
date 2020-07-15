from collections import deque

q = deque()
for _ in range(int(input().strip())):
    s = input().strip()
    if s.startswith("ISSUE"):
        q.appendleft(s[6:])
    elif s == "SOLVED":
        q.pop()
while len(q) > 0:
    print(q.pop())

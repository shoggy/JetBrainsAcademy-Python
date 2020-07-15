from collections import deque

q = deque()
for _ in range(int(input().strip())):
    s = input().strip()
    if s.startswith("READY "):
        q.appendleft(s.split()[1])
    elif s == "PASSED":
        print(q.pop())
    elif s == "EXTRA":
        q.appendleft(q.pop())

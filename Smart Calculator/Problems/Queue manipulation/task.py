from collections import deque

q = deque()
for _ in range(int(input().strip())):
    s = input().strip()
    if s.startswith("ENQUEUE"):
        q.appendleft(s.split()[1])
    elif s == "DEQUEUE":
        q.pop()
while len(q) > 0:
    print(q.pop())

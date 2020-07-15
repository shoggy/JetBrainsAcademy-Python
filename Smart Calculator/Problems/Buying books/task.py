from collections import deque

stack = deque()
n = int(input().strip())
for _ in range(n):
    s = input().strip()
    if s.startswith("BUY"):
        stack.append(s[4:])
    elif s == "READ":
        print(stack.pop())

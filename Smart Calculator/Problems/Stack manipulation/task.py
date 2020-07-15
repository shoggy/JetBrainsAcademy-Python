from collections import deque

stack = deque()
for _ in range(int(input().strip())):
    s = input().strip()
    if s.startswith("PUSH"):
        stack.append(s[5:])
    elif s == "POP":
        stack.pop()
while len(stack) > 0:
    print(stack.pop())

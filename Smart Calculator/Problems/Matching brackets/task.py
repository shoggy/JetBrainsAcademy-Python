# put your python code here
from collections import deque

opposites = {')': '(', ']': '[', '}': '{'}
stack = deque()
for c in input():
    if c in '([{':
        stack.append(c)
    elif c in ')]}':
        if len(stack) == 0 or opposites[c] != stack.pop():
            print("ERROR")
            break
else:
    if len(stack) == 0:
        print("OK")
    else:
        print("ERROR")

from collections import deque

n = int(input())

my_stack = deque()

for _ in range(n):
    my_stack.append(input())

while len(my_stack) > 0:
    print(my_stack.pop())

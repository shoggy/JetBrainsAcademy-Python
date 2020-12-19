# Write your code here
import random
import re
from collections import Counter


def numbers(user: int) -> None:
    secret = random.randint(0, 1_000_000)
    robot = random.randint(0, 1_000_000)
    print(f'The robot entered the number {robot}.')
    print(f'The goal number is {secret}.')
    if abs(secret - robot) < abs(secret - user):
        results['R'] += 1
        print('The robot won!')
    elif abs(secret - robot) > abs(secret - user):
        results['U'] += 1
        print('You won!')
    else:
        results['D'] += 1
        print("It's a draw!")


results = Counter()
while True:
    cmd = input('What is your number?\n')
    if cmd == 'exit game':
        break
    if not re.match(r'^-?\d.+$', cmd):
        print('A string is not a valid input!')
        continue
    cmd = int(cmd)
    if cmd < 0:
        print("The number can't be negative!")
    elif cmd > 1_000_000:
        print("Invalid input! The number can't be bigger than 1000000")
    else:
        numbers(cmd)

print(f'You won: {results["U"]},\n'
      f'The robot won: {results["R"]},\n'
      f'Draws: {results["D"]}.')

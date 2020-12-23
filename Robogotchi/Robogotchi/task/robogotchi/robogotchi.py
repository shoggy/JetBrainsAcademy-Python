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


def prenumber():
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


def rps(user: int):
    robot = random.randint(0, len(rps_obj) - 1)
    print(f'robot chose {rps_obj[robot]}')
    if robot == user:
        print("It's a draw!")
        results['D'] += 1
    elif (user + 1) % len(rps_obj) == robot:
        print('The robot won!')
        results['R'] += 1
    else:
        print('You won!')
        results['U'] += 1


def pre_rps():
    while True:
        cmd = input('What is your move?\n')
        if cmd == 'exit game':
            break
        if cmd not in rps_obj:
            print('No such option! Try again!')
        else:
            rps(rps_obj.index(cmd))


rps_obj = ["paper", "scissors", "rock"]
results = Counter()
cmd = input('Which game would you like to play?\n')
while True:
    if cmd == 'Rock-paper-scissors':
        pre_rps()
        break
    elif cmd == 'Numbers':
        prenumber()
        break
    else:
        cmd = input('Please choose a valid option: Numbers or Rock-paper-scissors?\n')

print(f'You won: {results["U"]},\n'
      f'The robot won: {results["R"]},\n'
      f'Draws: {results["D"]}.')

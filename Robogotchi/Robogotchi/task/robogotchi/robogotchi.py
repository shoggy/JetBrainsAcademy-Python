# Write your code here
import random
import re
from collections import Counter


class Numbers:
    results = Counter()

    @staticmethod
    def __numbers(user: int) -> None:
        secret = random.randint(0, 1_000_000)
        robot = random.randint(0, 1_000_000)
        print(f'The robot entered the number {robot}.')
        print(f'The goal number is {secret}.')
        if abs(secret - robot) < abs(secret - user):
            Numbers.results['R'] += 1
            print('The robot won!')
        elif abs(secret - robot) > abs(secret - user):
            Numbers.results['U'] += 1
            print('You won!')
        else:
            Numbers.results['D'] += 1
            print("It's a draw!")

    @staticmethod
    def play():
        Numbers.results = Counter()
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
                Numbers.__numbers(cmd)


class RockPaperScissors:
    RPS_OBJ = ["paper", "scissors", "rock"]
    results = Counter()

    @staticmethod
    def __rps(user: int):
        robot = random.randint(0, len(RockPaperScissors.RPS_OBJ) - 1)
        print(f'robot chose {RockPaperScissors.RPS_OBJ[robot]}')
        if robot == user:
            print("It's a draw!")
            RockPaperScissors.results['D'] += 1
        elif (user + 1) % len(RockPaperScissors.RPS_OBJ) == robot:
            print('The robot won!')
            RockPaperScissors.results['R'] += 1
        else:
            print('You won!')
            RockPaperScissors.results['U'] += 1

    @staticmethod
    def play():
        RockPaperScissors.results = Counter()
        while True:
            cmd = input('What is your move?\n')
            if cmd == 'exit game':
                break
            if cmd not in RockPaperScissors.RPS_OBJ:
                print('No such option! Try again!')
            else:
                RockPaperScissors.__rps(RockPaperScissors.RPS_OBJ.index(cmd))


class RoboPetException(Exception):

    def __init__(self, msg: str) -> None:
        super().__init__(msg)


class RoboPet:

    def __init__(self, name: str) -> None:
        super().__init__()
        self.name = name
        self.battery = 100
        self.overheat = 0
        self.skill = 0
        self.boredom = 0

    @classmethod
    def create(cls):
        name = input("How will you call your robot?\n")
        RoboPet(name).live()

    def print_info(self) -> None:
        print(f"{self.name}'s stats are:",
              f"battery is {self.battery},",
              f"overheat is {self.overheat},",
              f"skill level is {self.skill},",
              f"boredom is {self.boredom}.",
              sep='\n')

    def update_battery(self, x: int):
        new_battery = min(max(self.battery + x, 0), 100)
        if self.battery != new_battery:
            print(f"{self.name}'s level of the battery was {self.battery}. Now it is {new_battery}.")
            self.battery = new_battery

    def update_overheat(self, x: int):
        new_overheat = min(max(self.overheat + x, 0), 100)
        if new_overheat >= 100:
            raise RoboPetException(f"The level of overheat reached 100, {self.name} has blown up! "
                                   f"Game over. Try again?")
        if self.overheat != new_overheat:
            # TODO description has the-article
            print(f"{self.name}'s level of overheat was {self.overheat}. Now it is {new_overheat}.")
            self.overheat = new_overheat

    # def update_skill(self, x: int):
    #     new_skill = self.skill + x
    #     if not (0 <= new_skill <= 100):
    #         raise RoboPetException(f"Skill level is {new_skill}")
    #     print(f"{self.name}'s level of the skill was {self.skill}. Now it is {new_skill}.")
    #     self.skill = new_skill

    def update_boredom(self, x: int):
        new_boredom = min(max(0, self.boredom + x), 100)
        if self.boredom != new_boredom:
            print(f"{self.name}'s level of the boredom was {self.boredom}. Now it is {new_boredom}.")
            self.boredom = new_boredom

    def play(self):
        # TODO wrong text in description
        # cmd = input('Rock-paper-scissors or Numbers?\n')
        cmd = input('Which game would you like to play?\n')
        while True:
            if cmd == 'Rock-paper-scissors':
                RockPaperScissors.play()
                results = RockPaperScissors.results
                break
            elif cmd == 'Numbers':
                Numbers.play()
                results = Numbers.results
                break
            else:
                cmd = input('Please choose a valid option: Numbers or Rock-paper-scissors?\n')

        print(f'You won: {results["U"]},\n'
              # TODO the-article in description
              f'Robot won: {results["R"]},\n'
              f'Draws: {results["D"]}.')
        self.update_boredom(-20)
        self.update_overheat(10)

    def recharge(self):
        if self.battery >= 100:
            print(f'{self.name} is charged!')
        else:
            self.update_battery(10)
            self.update_overheat(-5)
            self.update_boredom(5)
            print(f'{self.name} is recharged!')

    def sleep(self):
        if self.overheat == 0:
            print(f'{self.name} is cool')
        else:
            self.update_overheat(-20)
            if self.overheat == 0:
                print(f'{self.name} is cool')
            else:
                print(f'{self.name} cooled off')

    def live(self):
        while True:
            print("",
                  f"Available interactions with {self.name}:",
                  "exit – Exit",
                  "info – Check the vitals",
                  "recharge – Recharge",
                  "sleep – Sleep mode",
                  "play – Play",
                  "",
                  sep='\n')
            cmd = input('Choose:\n')
            try:
                if cmd == 'exit':
                    print('Game over.')
                    break
                elif cmd == 'info':
                    self.print_info()
                elif cmd == 'recharge':
                    self.recharge()
                elif cmd == 'sleep':
                    self.sleep()
                elif cmd == 'play':
                    self.play()
                else:
                    print('Invalid input, try again!')
            except RoboPetException as e:
                print(e)
                break


if __name__ == '__main__':
    RoboPet.create()

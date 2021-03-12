from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, starting_sum, interest=None):
        self.sum = starting_sum
        self.interest = interest

    @abstractmethod
    def add_money(self, amount):
        ...

    def add_interest(self):
        ...


# create SavingsAccount and Deposit

class SavingsAccount(Account):
    def add_money(self, amount):
        if amount < 10:
            print('Cannot add to SavingsAccount: amount too low.')
        else:
            self.sum += amount


class Deposit(Account):
    def add_money(self, amount):
        if amount < 50:
            print('Cannot add to Deposit: amount too low.')
        else:
            self.sum += amount

    def add_interest(self):
        self.sum *= 1 + self.interest

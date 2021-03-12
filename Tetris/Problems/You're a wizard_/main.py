from abc import ABC, abstractmethod


class Player(ABC):
    def __init__(self, name, rank, level):
        self.name = name
        self.rank = rank
        self.level = level
        super().__init__()

    @abstractmethod
    def fight(self):
        ...

    @abstractmethod
    def do_spell(self):
        ...

    @staticmethod
    def sing_song():
        print("No songs for me!")


# create a Wizard

class Wizard(Player):
    def fight(self):
        print('wizard fight')

    def do_spell(self):
        print('wizard spell')

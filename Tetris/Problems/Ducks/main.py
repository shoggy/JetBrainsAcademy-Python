# create the hierarchy here
class Animal:
    ...


class FlyingAnimal(Animal):
    ...


class SwimmingAnimal(Animal):
    ...


class WalkingAnimal(Animal):
    ...


class Duck(FlyingAnimal, SwimmingAnimal, WalkingAnimal):
    ...

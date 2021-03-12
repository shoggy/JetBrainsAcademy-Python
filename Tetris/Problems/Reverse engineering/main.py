# create the hierarchy here
class Vehicle:
    pass


class LandVehicle(Vehicle):
    pass


class WaterVehicle(Vehicle):
    pass


class Car(LandVehicle):
    pass


class Boat(WaterVehicle):
    pass


class CarBoat(Car, Boat):
    pass

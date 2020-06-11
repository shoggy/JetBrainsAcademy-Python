import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def dist(self, b):
        d = math.sqrt((self.x - b.x) * (self.x - b.x)
                      + (self.y - b.y) * (self.y - b.y))
        return f'{d:.1f}'

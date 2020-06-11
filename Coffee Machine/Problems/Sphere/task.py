class Sphere:
    # finish class Sphere here
    PI = 3.1415

    def __init__(self, r):
        self.radius = r
        self.volume = Sphere.PI * r * r * r * 4 / 3

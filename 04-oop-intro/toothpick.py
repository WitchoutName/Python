import math as m
import random as r


class Toothpick:
    DEFAULT_RADIUS = 0.1
    DEFAULT_LENGTH = 5
    DEFAULT_MATERIAL = "wood"

    def __init__(self, **kwargs):
        self.radius = kwargs["radius"] if "radius" in kwargs else Toothpick.DEFAULT_RADIUS
        self.length = kwargs["length"] if "length" in kwargs else Toothpick.DEFAULT_LENGTH
        self.material = kwargs["material"] if "material" in kwargs else Toothpick.DEFAULT_MATERIAL

    def __str__(self):
        return f"r: {self.radius}cm, l: {self.length}cm, mat: {self.material}"

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __iadd__(self, other):
        self.radius += other.radius
        self.length += other.length
        return self

    def __isub__(self, other):
        self.radius -= other.radius
        self.length -= other.length
        return self

    @classmethod
    def default(cls):
        return cls(radius=cls.DEFAULT_RADIUS, length=cls.DEFAULT_LENGTH, material=cls.DEFAULT_MATERIAL)

    @staticmethod
    def random_material():
        return r.choice(["wood", "metal", "plastic", "glass"])

    def volume(self):
        return m.pi * pow(self.radius, 2) * self.length / 10 * 8 + m.pi * pow(self.radius, 2) * self.length / 10 / 3 * 2

    def surface(self):
        return 2 * m.pi * self.radius * self.length + m.pi * self.radius * m.sqrt(pow(self.radius, 2) + pow(self.length / 10, 2)) * 2


toothpick1 = Toothpick.default()
toothpick2 = Toothpick(length=45, radius=5, material=Toothpick.random_material())
print(f"toothpick1 = {toothpick1}")
print(f"toothpick2 = {toothpick2}")
print(f"toothpick1 > toothpick2: {toothpick1 > toothpick2}")
print(f"toothpick1 < toothpick2: {toothpick1 < toothpick2}")
print("* toothpick1 += toothpick2 *")
toothpick1 += toothpick2
print(f"toothpick1 = {toothpick1}")
print(f"tp1 volume: {toothpick1.volume()}cm3")
print(f"tp1 surface: {toothpick1.surface()}cm2")

import math as m
import random as r


class VirtualToothpick:
    DEFAULT_RADIUS = 0.1
    DEFAULT_LENGTH = 5
    DEFAULT_MATERIAL = "wood"

    def __init__(self, **kwargs):
        self.__radius = kwargs["radius"] if "radius" in kwargs else VirtualToothpick.DEFAULT_RADIUS
        self.__length = kwargs["length"] if "length" in kwargs else VirtualToothpick.DEFAULT_LENGTH

    def __str__(self):
        return f"r: {self.__radius}cm, l: {self.__length}cm"

    def __lt__(self, other):
        return self.volume() < other.volume()

    def __gt__(self, other):
        return self.volume() > other.volume()

    def __iadd__(self, other):
        self.__radius += other.radius
        self.__length += other.length
        return self

    def __isub__(self, other):
        self.__radius -= other.radius
        self.__length -= other.length
        return self

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        if isinstance(value, float):
            self.__radius = value

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if isinstance(value, float):
            self.__length = value

    @classmethod
    def default(cls):
        return cls(radius=cls.DEFAULT_RADIUS, length=cls.DEFAULT_LENGTH, material=cls.DEFAULT_MATERIAL)

    def volume(self):
        return m.pi * pow(self.__radius, 2) * self.__length / 10 * 8 + m.pi * pow(self.__radius, 2) * self.__length / 10 / 3 * 2

    def surface(self):
        return 2 * m.pi * self.__radius * self.__length + m.pi * self.__radius * m.sqrt(pow(self.__radius, 2) + pow(self.__length / 10, 2)) * 2


class RealToothpick(VirtualToothpick):
    def __init__(self, **kwargs):
        super().__init__(
            radius=kwargs["radius"] if "radius" in kwargs else VirtualToothpick.DEFAULT_RADIUS,
            length=kwargs["length"] if "length" in kwargs else VirtualToothpick.DEFAULT_LENGTH
        )
        self.material = kwargs["material"] if "material" in kwargs else VirtualToothpick.DEFAULT_MATERIAL

    def __str__(self):
        return f"r: {super().radius}cm, l: {super().length}cm, mat: {self.material}"

    @staticmethod
    def random_material():
        return r.choice(["wood", "metal", "plastic", "glass"])



toothpick1 = VirtualToothpick.default()
toothpick2 = VirtualToothpick(length=564, radius=456)
print(f"toothpick1 = {toothpick1}")
print(f"toothpick2 = {toothpick2}")
print(f"toothpick1 > toothpick2: {toothpick1 > toothpick2}")
print(f"toothpick1 < toothpick2: {toothpick1 < toothpick2}")
print("* toothpick1 += toothpick2 *")
toothpick1 += toothpick2
print(f"toothpick1 = {toothpick1}")
print(f"tp1 volume: {toothpick1.volume()}cm3")
print(f"tp1 surface: {toothpick1.surface()}cm2")
print(RealToothpick(length=45, material=RealToothpick.random_material()))

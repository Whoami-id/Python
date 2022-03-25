from math import sqrt
from functools import total_ordering
import builtins
import numbers


@total_ordering
class Vector2D:
    def __init__(self, x=0, y=0):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self.x = x
            self.y = y
        else:
            raise TypeError("you must pass int or float values for x and y")

    def __repr__(self):
        return "vector.Vector2D({}, {})".format(self.x, self.y)

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y = other.y
        return Vector2D(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vector2D(x, y)

    def __mul__(self, other):
        if isinstance(other, Vector2D):
            return self.x * other.x + self.y * other.y
        else:
            return Vector2D(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector2D(self.x / other, self.y / other)

    def __abs__(self):
        return sqrt(pow(self.x, 2) + pow(self.y, 2))

    def check_vector_type(self, vector2):
        if not isinstance(self, Vector2D) or not isinstance(vector2, Vector2D):
            raise TypeError("you have to compare two instance of vector class")

    def __eq__(self, other):
        self.check_vector_type(other)
        if self.x == other.x and self.y == other.y:
            return True
        else:
            return False

    def __bool__(self):
        return bool(abs(self))

    def __lt__(self, other):
        if abs(self) < abs(other):
            return True
        else:
            return False

    def __call__(self):
        print("Calling the __Call__")
        return self.__repr__()


v1 = Vector2D()

v2 = Vector2D(1, 1)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v2 / 5.0)
print(abs(v2))
print(v1 == v2)

print(v1 > v2)
print(v1 <= v2)
print(v1 > v2)
print(v1 >= v2)
print(v1 == v2)
print(v1 != v2)

v2()

v3 = Vector2D(3, 2)

print(dir(builtins))
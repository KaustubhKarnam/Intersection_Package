import numpy as np


class Point:
    """A point."""

    def __init__(self, point):
        self._point = np.array(point, dtype=float)

    def __repr__(self):
        return f"{self._point.tolist()}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self._point + other._vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other._vector + self._point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self._point - other._point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other._point, self._point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self._vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self._vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector + other._vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self._vector - other._vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other._vector, self._vector)
        return False

class Ray:
    """A ray."""
    def __init__(self, point, vector):
        self.point = point
        self.vector = vector
    
    def __repr__(self):
        return f"Origin({self.point}), Direction Vector({self.vector})"
    
    def __eq__(self, other):
        if np.array_equal(other.vector, self.vector) == True:
            if np.array_equal(other.point, self.point) == True:
                return True
            else:
                return False
        else:
            return False


class Sphere:
    """A sphere."""
    def __init__(self, point, radius):
        self.point = np.array(point)
        self.radius = radius
    
    def __repr__(self):
        return f"Center Point({self.point}), Radius({self.radius})"
    
    def __eq__(self, other):
        if np.array_equal(other.point, self.point) == True:
            if np.array_equal(other.radius, self.radius) == True:
                return True
            else:
                return False
        else:
            return False

class Triangle:
    """A triangle."""

    pass


"""Tests"""
p1 = Point((0,0,0))
r1 = 30.0
p2 = Point((0,0,0))
r2 = 30.0

s1 = Sphere(p1,r1)
s2 = Sphere(p2,r2)

print(s1)


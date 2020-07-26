import numpy as np
import math

class Point:
    """A point."""

    def __init__(self, point):
        self.point = np.array(point, dtype=float)

    def __repr__(self):
        return f"Point({self.point.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Point(self.point + other.vector)
        return NotImplemented

    def __radd__(self, other):
        if isinstance(other, Vector):
            return Point(other.vector + self.point)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Point):
            return Vector(self.point - other.point)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Point):
            return np.array_equal(other.point, self.point)
        return False


class Vector:
    """A vector."""

    def __init__(self, vector):
        self.vector = np.array(vector, dtype=float)

    def __repr__(self):
        return f"Vector({self.vector.tolist()})"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector + other.vector)
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Vector):
            return Vector(self.vector - other.vector)
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Vector):
            return np.array_equal(other.vector, self.vector)
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
    def get_vector(self):
        return(np.array(self.vector))

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
    def __init__(self, point1, point2, point3):
        self.point1 = np.array(point1)
        self.point2 = np.array(point2)
        self.point3 = np.array(point3)
         
"""Tests"""


def _intersect_ray_with_sphere(ray, sphere):
    u = ray.vector/np.linalg.norm(ray.vector)
    nabla = ((np.dot(u,(ray.point-sphere.point)))**2) - (np.dot((ray.point-sphere.point),(ray.point-sphere.point))-sphere.radius**2)
    if nabla > 0:
        d1 = -(np.dot(u,(ray.point-sphere.point)))+abs(math.sqrt(nabla))
        d2 = -(np.dot(u,(ray.point-sphere.point)))-abs(math.sqrt(nabla))
        return np.array((Point(ray.point+(d1*u)),Point(ray.point+(d2*u))))
    elif nabla == 0:
        d = -(np.dot(u,(ray.point-sphere.point)))
        return np.array(Point(ray.point+(d*u)))
    else:
        print("Ray does not intersect sphere")

r1 = Ray((-30,-30,0), (1,0,0))
s1 = Sphere((0,0,0),30)
print(_intersect_ray_with_sphere(r1,s1))

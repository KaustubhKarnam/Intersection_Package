from .objects import Point, Vector, Ray, Sphere, Triangle
import numpy as np
import math

def intersect(first_object, second_object):
    ...


def _intersect_ray_with_sphere(ray, sphere):
    u = ray.vector/np.linalg.norm(ray.vector)
    nabla = ((np.dot(u,(ray.point-sphere.point)))**2) - (np.dot((ray.point-sphere.point),(ray.point-sphere.point))-sphere.radius**2)
    if nabla > 0:
        d = np.array([-(np.dot(u,(ray.point-sphere.point)))+abs(math.sqrt(nabla)),-(np.dot(u,(ray.point-sphere.point)))-abs(math.sqrt(nabla))])
        value = []
        for d in d[d>=0]:
            value.append(Point(ray.point+(d*u)))
        return np.array(value)
    
    elif nabla == 0:
        d = -1*(np.dot(u,(ray.point-sphere.point)))
        return np.array(Point(ray.point+(d*u)))
    else:
        print("Ray does not intersect sphere")


def _intersect_ray_with_triangle(ray, triangle):
    ...

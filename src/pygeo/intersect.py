from .objects import Point, Vector, Ray, Sphere, Triangle
import numpy as np
import math
# def intersect(first_object, second_object):
#     ...


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
# def _intersect_ray_with_triangle(ray, triangle):
#     ...

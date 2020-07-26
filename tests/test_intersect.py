from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo.objects import Ray, Sphere, Triangle


# intersect


# _intersect_ray_with_sphere
def intersect_ray_with_sphere():
    r1 = Ray((-30,-30,0), (1,0,0))
    s1 = Sphere((0,0,0),30)
    _intersect_ray_with_sphere(r1,s1)


# _intersect_ray_with_triangle

from pygeo.intersect import (
    intersect,
    _intersect_ray_with_sphere,
    _intersect_ray_with_triangle,
)
from pygeo import Point, Vector, Ray, Sphere, Triangle
import numpy as np

# intersect


# _intersect_ray_with_sphere
def test__intersect_ray_with_sphere__one_point__return_true():
    assert (_intersect_ray_with_sphere(Ray((-3,1,0),(1,0,0)),Sphere((0,0,0),1.0)) == Point([0,1,0]))

def test__intersect_ray_with_sphere__two_points__return_true():
    assert np.array_equal(_intersect_ray_with_sphere(Ray((-2,0,0),(1,0,0)),Sphere((0,0,0),1.0)),[Point([1,0,0]),Point([-1,0,0])]) is True

def test__intersect_ray_with_sphere__no_points__return_true():
    assert (_intersect_ray_with_sphere(Ray((-2,1.5,0),(1,0,0)),Sphere((0,0,0),1.0)) == None)

def test__intersect_ray_with_sphere__ray_in_sphere__one_point__return_true():
    assert (_intersect_ray_with_sphere(Ray((-0.5,0,0),(1,0,0)),Sphere((0,0,0),1.0))==Point([1,0,0]))

def test__intersect_ray_with_sphere__ray_outside_sphere__one_point__return_true():
    assert (_intersect_ray_with_sphere(Ray((-3,1,0),(1,0,0)),Sphere((1,1,1),1.0))==Point([1,1,0]))

def test__intersect_ray_with_sphere__ray_outside_sphere__two_points__return_true():
    assert np.array_equal(_intersect_ray_with_sphere(Ray((-2,1,1),(1,0,0)),Sphere((1,1,1),1.0)),[Point([2,1,1]),Point([0,1,1])]) is True

def test__intersect_ray_with_sphere__ray_outside_sphere__no_points__return_true():
    assert (_intersect_ray_with_sphere(Ray((-2,1.5,0),(1,0,0)),Sphere((1,1,1),1.0)) == None)



# _intersect_ray_with_triangle




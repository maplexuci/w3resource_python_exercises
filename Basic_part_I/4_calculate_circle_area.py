# Write a Python program which accepts the radius of a circle
# from the user and compute the area.


from math import pi


def circle_area(radius):
    area = pi * radius**2

    return area


print(circle_area(1.1))

# Write a Python program to get the
# volume of a sphere with radius 6


from math import pi


def volume(radius):
    vol = 4/3 * pi * radius**3
    return vol


print(volume(6))

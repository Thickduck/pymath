from math import *


# basic arithmetic operations
def add(*numbers):
    result = 0
    for number in numbers:
        result += number
    return result


def multiply(*numbers):
    result = 1
    for number in numbers:
        result *= number
    return result


def divide(num1, num2):
    return num1 / num2


def sub(num1, num2):
    return num1 - num2

# exponential operators
# smol note: Don't use negative numbers! (only for cuberoot)


def root(num):
    return sqrt(num)


def sqr(num):
    return num * num


def cube(num):
    return num * num * num


def cuberoot(num):
    return num ** 1 / 3

# trignometry operators
# Take approx. because the conversion is 80% accurate!!!


def sine(num1):
    return sin(num1 * 0.017453)


def cosine(num):
    return cos(num * 0.017453)


def tangent(num):
    return tan(num * 0.017453)


# trignometric square calculators

def sinsqr(num):
    a = sin(num * 0.017453)
    b = a * a
    return b


def cossqr(num):
    a = cos(num * 0.017453)
    b = a ** 2
    return b


def tansqr(num):
    a = tan(num * 0.017453)
    b = a ** 2
    return b

def radsin(num):
    return sin(num)


def radcos(num):
    return cos(num)

def radtan(num):
    return tan(num)


def radsinsqr(num):
    a = sin(num)
    b = a ** 2
    return b


def radcossqr(num):
    a = cos(num)
    b = a ** 2


def radtansqr(num):
    a = tan(num)
    b = a ** 2


def triangle(angle1, angle2):
    missingangle = 180 - (angle1 + angle2)
    return missingangle

def quadrilateral(angle1, angle2, angle3):
    missingangle = 360 - (angle1 + angle2 + angle3)
    return missingangle

def pentagon(angle1, angle2, angle3, angle4):
    missingangle = 540 - (angle1 + angle2 + angle3 + angle4)
    return missingangle

def hexagon (angle1, angle2, angle3, angle4, angle5):
    missingangle = 720 - (angle1 + angle2 + angle3 + angle4 + angle5)
    return missingangle

def comp(angle):
    a = 90 - angle
    return a

def supp(angle):
    a = 180 - angle
    return a


def typeofangle(angle):
    if angle == 180:
        return str(angle) + ' Straight angle'

    elif angle == 90:
        return str(angle) + ' Right angle'

    elif angle == 360:
        return str(angle) + ' Complete angle'

    elif angle == 0:
        return str(angle) + ' No angle is formed!'

    elif angle > 90 and angle <180:
        return str(angle) + ' Obtuse angle'
   
    elif angle < 90:
        return str(angle) + ' Acute angle'

    elif angle > 180 and angle <360:
        return str(angle) + ' Reflex angle'

    elif angle > 360:
        raise ValueError('Please enter a valid input!')

    else:
        pass

def areasqr(side):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = side * side
        return str(n) + ' cm^2'

    elif a == 'm':
        n = side ** 2
        return str(n) + ' m^2'

    else:
        raise ValueError('Please enter a valid input!')

def arearect(length, breadth):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = length * breadth
        return str(n) + ' cm^2'

    elif a == 'm':
        n = length * breadth
        return str(n) + ' m^2'

    else:
        raise ValueError('Please enter a valid input!')

def areacircle(radius):
    a = str(input('(c)m or (m): '))
    if a == 'm':
        n = 3.142857142857 * (radius ** 2)
        return str(n) + ' m^2'

    elif a == 'c':
        n = 3.142857142857 * (radius ** 2)
        return str(n) + ' cm^2'

    else:
        raise ValueError('Please enter a valid input!')

def areaparellelogram(length, height):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = length * height
        return str(n) + ' cm^2'

    elif a == 'm':
        n = length * height
        return str(n) + ' m^2'

    else:
        raise ValueError('Please enter a valid input!')

def areatrapezium(parallelside1, parallelside2, height):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = 0.5 * (parallelside1 + parallelside2) * height
        return str(n) + ' cm^2'

    elif a == 'm':
        n = 0.5 * (parallelside1 + parallelside2) * height
        return str(n) + ' m^2'

    else:
        raise ValueError('Please enter a valid input!')

def persqr(side):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = 4 * side
        return str(n) + ' cm'

    elif a == 'm':
        n = 4 * side
        return str(n) + ' m'

    else:
        raise ValueError('Please enter a valid input!')

def perrect(length, breadth):
    a = str(input('(c)m or (m): '))
    if a == 'c':
        n = 2 * (length + breadth)
        return str(n) + ' cm'

    elif a == 'm':
        n = 2 * (length + breadth)
        return str(n) + ' m'

    else:
        raise ValueError('Please enter a valid input!')

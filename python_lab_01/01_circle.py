#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 01: площадь круга и попадание точек в круг.

Круг с центром в начале координат, радиус 42, число пи = 3.1415926.
Площадь выводится с точностью до 4 знаков после запятой.
"""

PI = 3.1415926

radius = 42
point_1 = (23, 34)
point_2 = (30, 30)


def circle_area(r, pi=PI):
    """Площадь круга радиуса r."""
    return pi * r * r


def point_in_circle(point, r):
    """True, если точка лежит внутри круга или на его границе.

    Сравниваются квадраты величин, поэтому извлекать корень не нужно.
    """
    x, y = point
    return x * x + y * y <= r * r


def run():
    print(round(circle_area(radius), 4))
    for point in (point_1, point_2):
        print(point_in_circle(point, radius))


if __name__ == '__main__':
    run()

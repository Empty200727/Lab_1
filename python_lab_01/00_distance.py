#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 00: таблица расстояний между городами.

Исходные данные - координаты городов на условной сетке. Нужно получить
словарь, где для каждого города хранится словарь расстояний до остальных.
"""

from itertools import combinations
from math import hypot

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}


def segment_length(start, end):
    """Евклидово расстояние между двумя точками плоскости."""
    return hypot(end[0] - start[0], end[1] - start[1])


def build_distance_table(coords):
    """Строит симметричную таблицу расстояний {город: {город: расстояние}}."""
    table = {city: {} for city in coords}
    for first, second in combinations(coords, 2):
        length = segment_length(coords[first], coords[second])
        table[first][second] = length
        table[second][first] = length
    return table


def run():
    for city, neighbours in build_distance_table(sites).items():
        row = ', '.join(f'{name}: {value:.2f}' for name, value in neighbours.items())
        print(f'{city} -> {row}')


if __name__ == '__main__':
    run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 04: список членов семьи и их рост.

Нужно вывести рост отца и суммарный рост всей семьи.
"""

my_family = ['Отец', 'Мать', 'Бабушка', 'Дедушка', 'Я']

my_family_height = [
    ['Отец', 178],
    ['Мать', 165],
    ['Бабушка', 160],
    ['Дедушка', 174],
    ['Я', 183],
]


def height_of(heights, member):
    """Ищет рост указанного члена семьи в списке списков."""
    for name, value in heights:
        if name == member:
            return value
    raise KeyError(member)


def total_height(heights):
    """Суммирует рост всех членов семьи."""
    total = 0
    for _, value in heights:
        total += value
    return total


def run():
    print(f'Рост отца - {height_of(my_family_height, "Отец")} см')
    print(f'Общий рост моей семьи - {total_height(my_family_height)} см')


if __name__ == '__main__':
    run()

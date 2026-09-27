#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 03: извлечение фильмов из строки только с помощью срезов.

Методы строк (split, find и т.п.) использовать запрещено,
исходную строку менять нельзя, запятые не выводятся.
"""

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'


def pick_movies(line):
    """Возвращает словарь: первый, последний, второй и предпоследний фильмы."""
    return {
        'first': line[:10],
        'last': line[-15:],
        'second': line[12:25],
        'penultimate': line[-22:-17],
    }


def run():
    for title in pick_movies(my_favorite_movies).values():
        print(title)


if __name__ == '__main__':
    run()

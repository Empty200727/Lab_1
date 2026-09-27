#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 06: суммарная длительность песен альбома Violator.

Данные даны дважды: в виде списка списков и в виде словаря.
Суммы округляются до 3 знаков, чтобы убрать погрешность float.
"""

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

LIST_TITLES = ('Halo', 'Enjoy the Silence', 'Clean')
DICT_TITLES = ('Sweetest Perfection', 'Policy of Truth', 'Blue Dress')


def duration_from_list(songs, titles):
    """Сумма длительностей выбранных песен из списка пар [название, время]."""
    total = 0
    for title, minutes in songs:
        if title in titles:
            total += minutes
    return round(total, 3)


def duration_from_dict(songs, titles):
    """Сумма длительностей выбранных песен из словаря {название: время}."""
    return round(sum(songs[title] for title in titles), 3)


def run():
    print(f'Три песни звучат {duration_from_list(violator_songs_list, LIST_TITLES)} минут')
    print(f'А другие три песни звучат {duration_from_dict(violator_songs_dict, DICT_TITLES)} минут')


if __name__ == '__main__':
    run()

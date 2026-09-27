#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 08: цветы сада и луга как множества."""

garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

garden_set = set(garden)
meadow_set = set(meadow)


def all_flowers(first, second):
    return set(first).union(second)


def common_flowers(first, second):
    return set(first).intersection(second)


def only_in(first, second):
    """Цветы, которые есть в first, но отсутствуют в second."""
    return set(first).difference(second)


def run():
    print('Все виды цветов:', all_flowers(garden_set, meadow_set))
    print('Растут и там и там:', common_flowers(garden_set, meadow_set))
    print('Только в саду:', only_in(garden_set, meadow_set))
    print('Только на лугу:', only_in(meadow_set, garden_set))


if __name__ == '__main__':
    run()

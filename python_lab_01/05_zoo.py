#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 05: изменение списка животных в зоопарке.

1) посадить медведя между львом и кенгуру;
2) добавить птиц в последние клетки;
3) убрать слона;
4) узнать номера клеток льва и жаворонка (нумерация с 1).
"""

zoo = ['lion', 'kangaroo', 'elephant', 'monkey']
birds = ['rooster', 'ostrich', 'lark']


def zoo_steps(animals, new_birds):
    """Возвращает список состояний зоопарка после каждого шага."""
    cages = list(animals)
    steps = []

    cages[1:1] = ['bear']
    steps.append(list(cages))

    cages.extend(new_birds)
    steps.append(list(cages))

    del cages[cages.index('elephant')]
    steps.append(list(cages))

    return steps


def cage_of(cages, animal):
    """Номер клетки животного, начиная с единицы."""
    return cages.index(animal) + 1


def run():
    steps = zoo_steps(zoo, birds)
    for state in steps:
        print(state)
    final = steps[-1]
    print(f'Лев сидит в клетке №{cage_of(final, "lion")}')
    print(f'Жаворонок сидит в клетке №{cage_of(final, "lark")}')


if __name__ == '__main__':
    run()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Верхнеуровневый модуль лабораторной работы № 1.

Находит все модули-задания в пакете python_lab_01 и запускает их функцию run().
Примеры:
    python main.py          - запустить все задания по порядку
    python main.py 3 7      - запустить только задания 03 и 07
    python main.py --list   - показать список доступных заданий
"""

import argparse
import importlib
import pkgutil

import python_lab_01

PACKAGE = python_lab_01.__name__


def discover_tasks():
    """Возвращает отсортированные имена модулей-заданий пакета."""
    names = [info.name for info in pkgutil.iter_modules(python_lab_01.__path__)]
    return sorted(name for name in names if name[:2].isdigit())


def load_task(name):
    # Имя модуля начинается с цифры, поэтому обычный import не подходит.
    return importlib.import_module(f'{PACKAGE}.{name}')


def select_tasks(all_tasks, numbers):
    if not numbers:
        return all_tasks
    wanted = {f'{number:02d}' for number in numbers}
    return [name for name in all_tasks if name[:2] in wanted]


def parse_args(argv=None):
    parser = argparse.ArgumentParser(description='Запуск заданий ЛР № 1')
    parser.add_argument('numbers', nargs='*', type=int, help='номера заданий')
    parser.add_argument('--list', action='store_true', help='вывести список заданий')
    return parser.parse_args(argv)


def main(argv=None):
    args = parse_args(argv)
    tasks = discover_tasks()

    if args.list:
        print('\n'.join(tasks))
        return

    for name in select_tasks(tasks, args.numbers):
        print(f'----- {name} -----')
        load_task(name).run()
        print()


if __name__ == '__main__':
    main()

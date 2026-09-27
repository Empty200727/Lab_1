#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Задание 10: остатки и стоимость товаров на складе.

Формат вывода: <товар> - <кол-во> шт, стоимость <сумма> руб
"""

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}


def batch_totals(batches):
    """Возвращает (общее количество, общая стоимость) по списку партий."""
    count = sum(batch['quantity'] for batch in batches)
    cost = sum(batch['quantity'] * batch['price'] for batch in batches)
    return count, cost


def stock_report(names, warehouse):
    """Сводка по складу: {товар: (количество, стоимость)}."""
    return {name: batch_totals(warehouse[code]) for name, code in names.items()}


def run():
    for name, (count, cost) in stock_report(goods, store).items():
        print(f'{name} - {count} шт, стоимость {cost} руб')


if __name__ == '__main__':
    run()

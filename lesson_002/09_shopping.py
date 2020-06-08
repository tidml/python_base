#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь магазинов с распродажами

shops = {
    'ашан':
        [
            {'name': 'печенье', 'price': 10.99},
            {'name': 'конфеты', 'price': 34.99},
            {'name': 'карамель', 'price': 45.99},
            {'name': 'пирожное', 'price': 67.99}
        ],
    'пятерочка':
        [
            {'name': 'печенье', 'price': 9.99},
            {'name': 'конфеты', 'price': 32.99},
            {'name': 'карамель', 'price': 46.99},
            {'name': 'пирожное', 'price': 59.99}
        ],
    'магнит':
        [
            {'name': 'печенье', 'price': 11.99},
            {'name': 'конфеты', 'price': 30.99},
            {'name': 'карамель', 'price': 41.99},
            {'name': 'пирожное', 'price': 62.99}
        ],
}

from pprint import pprint

shops_list = list(shops.keys())
ashan_list = list(shops['ашан'][0:4])
pyaterochka_list = list(shops['пятерочка'][0:4])
magnit_list = list(shops['магнит'][0:4])

# Создайте словарь цен на продкты следующего вида (писать прямо в коде)
sweets = {
    ashan_list[0]['name']: [
        {'shop': shops_list[0], 'price': ashan_list[0]['price']},
        # {'shop': shops_list[1], 'price': pyaterochka_list[0]['price']},
        {'shop': shops_list[2], 'price': magnit_list[0]['price']},
    ],
    ashan_list[1]['name']: [
        # {'shop': shops_list[0], 'price': ashan_list[1]['price']},
        {'shop': shops_list[1], 'price': pyaterochka_list[1]['price']},
        {'shop': shops_list[2], 'price': magnit_list[1]['price']},
    ],
    ashan_list[2]['name']: [
        {'shop': shops_list[0], 'price': ashan_list[2]['price']},
        # {'shop': shops_list[1], 'price': pyaterochka_list[2]['price']},
        {'shop': shops_list[2], 'price': magnit_list[2]['price']},
    ],
    ashan_list[3]['name']: [
        # {'shop': shops_list[0], 'price': ashan_list[3]['price']},
        {'shop': shops_list[1], 'price': pyaterochka_list[3]['price']},
        {'shop': shops_list[2], 'price': magnit_list[3]['price']},
    ],
}
# Указать надо только по 2 магазина с минимальными ценами
pprint(sweets)

#зачет!
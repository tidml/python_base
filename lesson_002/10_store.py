#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

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

# Рассчитать на какую сумму лежит каждого товара на складе
# например для ламп

lamps_cost = store[goods['Лампа']][0]['quantity'] * store[goods['Лампа']][0]['price']
# или проще (/сложнее ?)
lamp_code = goods['Лампа']
lamps_item = store[lamp_code][0]
lamps_quantity = lamps_item['quantity']
lamps_price = lamps_item['price']
lamps_cost = lamps_quantity * lamps_price
print(f'Лампа - {lamps_quantity} шт, стоимость {lamps_cost} руб', ' ', sep = "\n")

# Вывести стоимость каждого вида товара на складе:
# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.

#РАСЧЕТ ПО СТОЛАМ

# кол-во столов на 1 складе
table1_quantity = store[goods['Стол']][0]['quantity']
# кол-во столов на 2 складе
table2_quantity = store[goods['Стол']][1]['quantity']

# общая стоимость столов на 1 складе
table1_cost = store[goods['Стол']][0]['price'] * table1_quantity
# общая стоимость столов на 2 складе
table2_cost = store[goods['Стол']][1]['price'] * table2_quantity

total_number_tables = table1_quantity + table2_quantity
total_cost_tables = table1_cost + table2_cost

print(f'Стоимость столов на 1 складе: {table1_cost} руб',
      f'Стоимость столов на 2 складе: {table2_cost} руб',
      f'Общее количество столов: {total_number_tables} шт, общая стоимость: {total_cost_tables} руб', ' ', sep = "\n")

#РАСЧЕТ ПО ДИВАНАМ

# кол-во диванов на 1 складе
sofa1_quantity = store[goods['Диван']][0]['quantity']
# кол-во диванов на 2 складе
sofa2_quantity = store[goods['Диван']][1]['quantity']

# общая стоимость диванов на 1 складе
sofa1_cost = store[goods['Диван']][0]['price'] * sofa1_quantity
# общая стоимость диванов на 2 складе
sofa2_cost = store[goods['Диван']][1]['price'] * sofa2_quantity

total_number_sofa = sofa1_quantity + sofa2_quantity
total_cost_sofa = sofa1_cost + sofa2_cost

print(f'Стоимость диванов на 1 складе: {sofa1_cost} руб',
      f'Стоимость диванов на 2 складе: {sofa2_cost} руб',
      f'Общее количество диванов: {total_number_sofa} шт, общая стоимость: {total_cost_sofa} руб', ' ', sep = "\n")

#РАСЧЕТ ПО СТУЛЬЯМ

# кол-во стульев на 1 складе
chairs1_quantity = store[goods['Стул']][0]['quantity']
# кол-во стульев на 2 складе
chairs2_quantity = store[goods['Стул']][1]['quantity']
# кол-во стульев на 3 складе
chairs3_quantity = store[goods['Стул']][2]['quantity']

# общая стоимость стульев на 1 складе
chairs1_cost = store[goods['Стул']][0]['price'] * chairs1_quantity
# общая стоимость стульев на 2 складе
chairs2_cost = store[goods['Стул']][1]['price'] * chairs2_quantity
# общая стоимость стульев на 3 складе
chairs3_cost = store[goods['Стул']][2]['price'] * chairs3_quantity

total_number_chairs = chairs1_quantity + chairs2_quantity + chairs3_quantity
total_cost_chairs = chairs1_cost + chairs2_cost + chairs3_cost

print(f'Стоимость стульев на 1 складе: {chairs1_cost} руб',
      f'Стоимость стульев на 2 складе: {chairs2_cost} руб',
      f'Стоимость стульев на 3 складе: {chairs3_cost} руб',
      f'Общее количество стульев: {total_number_chairs} шт, общая стоимость: {total_cost_chairs} руб', ' ',sep = "\n")

##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

#зачет!
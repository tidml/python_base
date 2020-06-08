#!/usr/bin/env python
# -*- coding: utf-8 -*-

# есть список животных в зоопарке

zoo = ['lion', 'kangaroo', 'elephant', 'monkey', ]

# посадите медведя (bear) между львом и кенгуру
#  и выведите список на консоль

zoo.insert(2, 'bear')
print(zoo)

# добавьте птиц из списка birds в последние клетки зоопарка
birds = ['rooster', 'ostrich', 'lark', ]
#  и выведите список на консоль

zoo.extend(birds)
print(zoo)

# уберите слона
#  и выведите список на консоль

zoo.pop(3)
# zoo.remove('elephant')
print(zoo)

# выведите на консоль в какой клетке сидит лев (lion) и жаворонок (lark).
# Номера при выводе должны быть понятны простому человеку, не программисту.

lion_position = zoo.index('lion') + 1
lark_position = zoo.index('lark') + 1
print(f'Лев сидит в клетке: #{str(lion_position)}', f'Жаворонок сидит в клетке: #{str(lark_position)}', sep="\n")

#зачет!
# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:

    def __add__(self, other):
        new_object = None
        if isinstance(other, Fire):
            new_object = Steam()
        elif isinstance(other, Air):
            new_object = Storm()
        elif isinstance(other, Earth):
            new_object = Dirt()
        return new_object

    def __str__(self):
        return 'Вода'


class Air:
    def __add__(self, other):
        new_object = None
        if isinstance(other, Fire):
            new_object = Lightning()
        elif isinstance(other, Earth):
            new_object = Dust()
        elif isinstance(other, Water):
            new_object = Storm()
        return new_object

    def __str__(self):
        return 'Воздух'


class Fire:

    def __add__(self, other):
        new_object = None
        if isinstance(other, Earth):
            new_object = Magma()
        elif isinstance(other, Water):
            new_object = Steam()
        if isinstance(other, Air):
            new_object = Lightning()
        return new_object

    def __str__(self):
        return 'Огонь'


class Earth:

    def __add__(self, other):
        new_object = None
        if isinstance(other, Fire):
            new_object = Magma()
        elif isinstance(other, Air):
            new_object = Dust()
        elif isinstance(other, Water):
            new_object = Dirt()
        return new_object

    def __str__(self):
        return 'Земля'


class Steam:

    def __str__(self):
        return 'Пар'


class Storm:

    def __str__(self):
        return 'Шторм'


class Dirt:

    def __str__(self):
        return 'Грязь'


class Lightning:

    def __str__(self):
        return 'Молния'


class Dust:

    def __str__(self):
        return 'Пыль'


class Magma:

    def __str__(self):
        return 'Лава'


print(Water(), '+', Fire(), '=', Water() + Fire())
print(Water(), '+', Air(), '=', Water() + Air())
print(Water(), '+', Earth(), '=', Water() + Earth())
print(Air(), '+', Fire(), '=', Air() + Fire())
print(Air(), '+', Earth(), '=', Air() + Earth())
print(Fire(), '+', Earth(), '=', Fire() + Earth())
print(Fire(), '+', Dust(), '=', Fire() + Dust())

# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
#Зачет!
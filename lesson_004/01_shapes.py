# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

def drawing_a_shape(point, number_of_sides, length):
    last_line_end_point = point
    the_sum_of_the_angles = int(180 * (number_of_sides - 2))
    range_step = int(180 - (the_sum_of_the_angles / number_of_sides))
    for angle in range(0, 360 - range_step, range_step):
        side = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        side.draw()
        point = side.end_point
    sd.line(start_point=point, end_point=last_line_end_point, width=3)


def triangle(point, length):
    drawing_a_shape(point=point, number_of_sides=3, length=length)


def square(point, length):
    drawing_a_shape(point=point, number_of_sides=4, length=length)


def pentagon(point, length):
    drawing_a_shape(point=point, number_of_sides=5, length=length)


def hexagon(point, length):
    drawing_a_shape(point=point, number_of_sides=6, length=length)


# Я имел ввиду вот это)
point = sd.get_point(100, 100)
triangle(point, 200)
point = sd.get_point(350, 100)
square(point, 200)
point = sd.get_point(630, 100)
pentagon(point, 130)
point = sd.get_point(900, 100)
hexagon(point, 100)

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


sd.pause()
#зачет!
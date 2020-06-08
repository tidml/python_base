# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

def drawing_a_shape(point, number_of_sides, length, color):
    last_line_end_point = point
    the_sum_of_the_angles = int(180 * (number_of_sides - 2))
    range_step = int(180 - (the_sum_of_the_angles / number_of_sides))
    for angle in range(0, 360 - range_step, range_step):
        side = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        side.draw(color=color)
        point = side.end_point
    sd.line(start_point=point, end_point=last_line_end_point, color=color, width=3)


def triangle(length, color):
    point = sd.get_point(100, 100)
    drawing_a_shape(point=point, number_of_sides=3, length=length, color=color)


def square(length, color):
    point = sd.get_point(350, 100)
    drawing_a_shape(point=point, number_of_sides=4, length=length, color=color)


def pentagon(length, color):
    point = sd.get_point(630, 100)
    drawing_a_shape(point=point, number_of_sides=5, length=length, color=color)


def hexagon(length, color):
    point = sd.get_point(900, 100)
    drawing_a_shape(point=point, number_of_sides=6, length=length, color=color)


shapes = {0: {'shape_name': 'треугольник', 'def_name': triangle},
          1: {'shape_name': 'квадрат', 'def_name': square},
          2: {'shape_name': 'пятиугольник', 'def_name': pentagon},
          3: {'shape_name': 'шестиугольник', 'def_name': hexagon}}


def draw_shapes():
    print('Возможные фигуры: ')
    for number, shape in shapes.items():
        print(number, shape['shape_name'])
    user_input = int(input('Введите номер фигуры: '))
    while user_input not in shapes:
        print('Ошибка! Введите число из предложенных')
        user_input = int(input('Введите номер фигуры: '))
    else:
        shapes[user_input]['def_name'](length=150, color=sd.COLOR_YELLOW)


draw_shapes()

sd.pause()

#зачет!
# -*- coding: utf-8 -*-
import simple_draw as sd

sd.resolution = (1200, 600)


# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg

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


colors = {0: {'color_name': 'red', 'sd_name': sd.COLOR_RED}, 1: {'color_name': 'orange', 'sd_name': sd.COLOR_ORANGE},
          2: {'color_name': 'yellow', 'sd_name': sd.COLOR_YELLOW},
          3: {'color_name': 'green', 'sd_name': sd.COLOR_GREEN},
          5: {'color_name': 'blue', 'sd_name': sd.COLOR_BLUE}, 6: {'color_name': 'purple', 'sd_name': sd.COLOR_PURPLE}}


def colored_shapes():
    print('Возможные цвета: ')
    for number, color in colors.items():
        print(number, color['color_name'])
    user_input = int(input('Введите номер цвета: '))
    while user_input not in colors:
        print('Ошибка! Введите число из предложенных')
        user_input = int(input('Введите номер цвета: '))
    else:
        length = 150
        triangle(length, colors[user_input]['sd_name'])
        square(length, colors[user_input]['sd_name'])
        pentagon(length - 50, colors[user_input]['sd_name'])
        hexagon(length - 50, colors[user_input]['sd_name'])


colored_shapes()
sd.pause()
# зачет!

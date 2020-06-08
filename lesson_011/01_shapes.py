# -*- coding: utf-8 -*-

import simple_draw as sd


# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def drawing_shape(point, angle, length, sides=n):
        last_line_end_point = point
        the_sum_of_the_angles = int(180 * (n - 2))
        range_step = int(180 - (the_sum_of_the_angles / n))
        for side in range(sides - 1):
            side = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
            side.draw()
            angle += range_step
            point = side.end_point
        sd.line(start_point=point, end_point=last_line_end_point, width=3)

    return drawing_shape


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
#зачет!
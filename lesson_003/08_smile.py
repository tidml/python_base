# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd
sd.resolution = (1200, 600)

# Написать функцию отрисовки смайлика по заданным координатам
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.

def smile(x, y):
    face_point = sd.get_point(x, y)
    left_eye_point = sd.get_point(x - 30, y + 20)
    right_eye_point = sd.get_point(x + 30, y + 20)
    color = (255, 255, 255)
    start_point = sd.get_point(x - 20, y - 30)
    end_point = sd.get_point(x + 20, y - 30)
    sd.circle(face_point, 70, color, 2)
    sd.circle(left_eye_point, 10, color, 1)
    sd.circle(right_eye_point, 10, color, 1)
    sd.line(start_point, end_point, color, 2)


def random_smiles(quantity):
    for _ in range(quantity):
        point = sd.random_point()
        smile(point.x, point.y)


random_smiles(10)

sd.pause()
#зачет!
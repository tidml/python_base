# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения


def draw_branches(point, angle, length):
    if length < 10:
        return
    branch = sd.get_vector(point, angle, length, 1)
    branch.draw()
    next_point = branch.end_point
    angle_for_right_branch = angle - 30
    angle_for_left_branch = angle + 30
    next_length = length * 0.75
    draw_branches(next_point, angle_for_right_branch, next_length)
    draw_branches(next_point, angle_for_left_branch, next_length)


root_point = sd.get_point(600, 30)


# draw_branches(point=root_point, angle=90, length=200)


# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_random_branches(point, angle, length):
    if length < 10:
        return
    branch = sd.get_vector(point, angle, length, 1)
    branch.draw()
    angel_delta = sd.random_number(18, 42)
    length_delta = sd.random_number(60, 90) / 100
    next_point = branch.end_point
    angle_for_right_branch = angle - angel_delta
    angle_for_left_branch = angle + angel_delta
    next_length = length * length_delta
    draw_random_branches(next_point, angle_for_right_branch, next_length)
    draw_random_branches(next_point, angle_for_left_branch, next_length)


root_point = sd.get_point(600, 30)
draw_random_branches(root_point, angle=90, length=200)

sd.pause()
#Зачет!
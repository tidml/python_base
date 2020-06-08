# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 255, 255)

# Нарисовать пузырек - три вложенных окружностей с шагом 5 пикселей
point = sd.get_point(100, 100)
radius = 50
for _ in range(3):
    radius += 5
    sd.circle(point, radius)

sd.sleep(2)


# Написать функцию рисования пузырька, принммающую 3 (или более) параметра: точка рисования, шаг и цвет

def bubble(point, step, color):
    radius = 30
    for _ in range(3):
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=2)


point = sd.get_point(600, 300)
color = (0, 0, 255)

sd.clear_screen()
bubble(point, 10, color)
sd.sleep(2)


# Нарисовать 10 пузырьков в ряд
def ten_bubbles():
    for x in range(100, 1200, 110):
        point = sd.get_point(x, 300)
        bubble(point, 10, color=(0, 0, 0))


sd.clear_screen()
ten_bubbles()
sd.sleep(3)


# Нарисовать три ряда по 10 пузырьков
def three_rows_of_ten_bubbles():
    for y in range(200, 500, 100):
        for x in range(100, 1200, 110):
            point = sd.get_point(x, y)
            bubble(point, 10, color=(0, 0, 0))


sd.clear_screen()
three_rows_of_ten_bubbles()
sd.sleep(2)


# Нарисовать 100 пузырьков в произвольных местах экрана случайными цветами
def random_bubbles(quantity):
    for _ in range(quantity):
        point = sd.random_point()
        colors = sd.random_color()
        bubble(point, 10, color=colors)


sd.clear_screen()
random_bubbles(100)

sd.pause()
#зачет!
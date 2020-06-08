# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1200, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:

    def __init__(self):
        self.x = sd.random_number(0, 1200)
        self.y = sd.random_number(0, 600)
        self.size = sd.random_number(10, 50)
        self.length = round(sd.random_number(10, 90) / 100, 1)

    def append(self, y):
        self.x = sd.random_number(0, 1200)
        self.y = y
        self.size = sd.random_number(10, 50)
        self.length = round(sd.random_number(10, 90) / 100, 1)

    def draw(self, color):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.size, color=color, factor_b=self.length)

    def clear_previous_picture(self):
        sd.start_drawing()
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.size, color=sd.background_color, factor_b=self.length)
        sd.finish_drawing()

    def move(self):
        self.y -= 5

    def can_fall(self):
        if self.y >= -50:  # Сделал специально, чтобы не оставлять снежинки внизу экрана
            return self.y >= -50


# flake = Snowflake()
# flake.create()
#
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw(color=sd.COLOR_WHITE)
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

flakes_list = []
fallen_flakes_list = []


def get_flakes(quantity):
    global flakes_list
    for _ in range(quantity):
        flake = Snowflake()
        flakes_list.append(flake)


def get_fallen_flakes():
    global flakes_list, fallen_flakes_list
    fallen_flakes_list = []
    for i, flake in enumerate(flakes_list):
        if not flake.can_fall():
            fallen_flakes_list.append(i)
    return fallen_flakes_list


def delete_snowflakes():
    global fallen_flakes_list
    for index in reversed(fallen_flakes_list):
        flakes_list.pop(index)

# 1) Получит список индексов параметром
# 2) Перевернет его
# 3) Удалит в цикле по списку индексов снежинки из списка снежинок


def append_flakes():
    global flakes_list
    for _ in fallen_flakes_list:
        flake = Snowflake()
        flake.append(600)
        flakes_list.append(flake)


get_flakes(20)

while True:
    for flake in flakes_list:
        flake.clear_previous_picture()
        flake.move()
        flake.draw(color=sd.COLOR_WHITE)
    fallen_flakes = get_fallen_flakes()
    if fallen_flakes:
        append_flakes()
        delete_snowflakes()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()
#зачет!
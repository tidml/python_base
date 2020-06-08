# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import add_snowflakes, color_snowflakes, move_snowflakes, fallen_snowflakes, delete_snowflake

sd.resolution = (1200, 600)

# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
add_snowflakes(20)
while True:
    #  нарисовать_снежинки_цветом(color=sd.background_color)
    #  сдвинуть_снежинки()
    #  нарисовать_снежинки_цветом(color)
    #  если есть номера_достигших_низа_экрана() то
    #       удалить_снежинки(номера)
    #       создать_снежинки(count)
    color_snowflakes(sd.background_color)
    move_snowflakes()
    color_snowflakes()
    fallen_snowflakes()
    number_of_fallen_snowflakes = fallen_snowflakes()
    if number_of_fallen_snowflakes > 0:
        add_snowflakes(number_of_fallen_snowflakes)
    delete_snowflake()
    # количество_упавших_снежинок = fallen_snowflakes()
    # если количество_упавших_снежинок > 0:
    #     add_snowflakes(количество_упавших_снежинок)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
#зачет!
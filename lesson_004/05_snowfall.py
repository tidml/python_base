# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

N = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()


def snowflakes(quantity):
    x_list = []
    y_list = []
    size_list = []
    length_list = []
    for _ in range(quantity):
        new_x = sd.random_number(50, 1150)
        x_list.append(new_x)
        new_y = sd.random_number(0, 600)
        y_list.append(new_y)
        new_size = sd.random_number(10, 40)
        size_list.append(new_size)
        new_length = round(sd.random_number(10, 90) / 100, 1)
        length_list.append(new_length)
    while True:
        sd.start_drawing()
        sd.clear_screen()
        for i, x in enumerate(x_list):
            if y_list[i] < 0:
                y_list[i] = 600
            point = sd.get_point(x_list[i], y_list[i])
            sd.snowflake(center=point, length=size_list[i], factor_b=length_list[i])
            y_list[i] -= 10
        sd.finish_drawing()
        sd.sleep(0.1)
        if sd.user_want_exit():
            break


snowflakes(20)

sd.pause()


# while True:
#     sd.clear_screen()
#     #
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break
# sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


#зачет!
# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for

sd.resolution = (1200, 600)
sd.background_color = (255, 255, 255)


def bricks_in_row():
    for row, y in enumerate(range(0, 600, 60)):
        x0 = 60 if row % 2 == 0 else 0  # "фишечка" интересная, в таких случаях очень помогает # Крутая! Проще в чтение
        for x in range(x0, 1200, 120):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + 120, y + 60)
            sd.rectangle(left_bottom, right_top, (0, 0, 0), width=2)


bricks_in_row()

sd.pause()

#зачет!
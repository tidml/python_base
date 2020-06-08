# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (0, 0, 0)

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

def rainbow_lines():
    x = 100
    for color in rainbow_colors:
        start_point = sd.get_point(x, 100)
        end_point = sd.get_point(x + 200, 500)
        sd.line(start_point, end_point, color=color, width=80)
        x += 80


rainbow_lines()
sd.sleep(2)


# Подсказка: цикл нужно делать сразу по тьюплу с цветами радуги.


# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво

def rainbow():
    radius = 100
    for color in rainbow_colors:
        point = sd.get_point(600, 0)
        sd.circle(point, radius, color, width=60)
        radius += 60


sd.clear_screen()
rainbow()

sd.pause()

#зачет!
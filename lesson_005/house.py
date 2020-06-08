import simple_draw as sd
from picture_items import wall as w


def square(start_x, length_x, height):
    point = sd.get_point(start_x, 0)
    last_line_end_point = point
    for number, angle in enumerate(range(0, 270, 90)):
        if number % 2 != 0:
            length = height + 7
        else:
            length = length_x + 7
        side = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        side.draw(color=sd.COLOR_BLACK)
        point = side.end_point
    sd.line(start_point=point, end_point=last_line_end_point, color=sd.COLOR_BLACK, width=3)


def window(start_x, length, height):
    point = sd.get_point(start_x + (length / 3), height / 4)
    sd.square(left_bottom=point, side=length / 3, color=sd.COLOR_WHITE, width=0)


def roof(start_x, length, height):
    point = sd.get_point(start_x + (length * 1.15), height + 7)
    last_line_end_point = point
    for angle in range(150, 230, 60):
        side = sd.get_vector(start_point=point, angle=angle, length=length * 0.75, width=3)
        side.draw(color=sd.COLOR_BLACK)
        point = side.end_point
    sd.line(start_point=point, end_point=last_line_end_point, color=sd.COLOR_BLACK, width=3)


def house(start_x, length, height):
    square(start_x, length, height)
    w.wall(start_x, length, height, 11)
    window(start_x, length, height)
    roof(start_x, length, height)


# sd.resolution = (1200, 600)
# sd.background_color = (255, 255, 255)
# house(250, 300, 180)
# sd.pause()
import simple_draw as sd

rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow(start_x, radius=400):
    for color in rainbow_colors:
        point = sd.get_point(start_x, 0)
        sd.circle(point, radius, color, width=10)
        radius += 10


def sky(start_y):
    color = (216, 243, 246)
    point = sd.get_point(x=0, y=start_y)
    sd.square(left_bottom=point, side=1200, color=color, width=0)


def sun(start_x, start_y, size):
    radius = size
    point = sd.get_point(start_x, start_y)
    sd.circle(point, radius, sd.COLOR_YELLOW, width=0)
    sd.snowflake(point, radius * 2.1, sd.COLOR_YELLOW, 0.1, 0.1)


if __name__ == "__main__":
    sd.resolution = (1200, 600)
    sd.background_color = (0, 0, 0)
    sun(100, 400, 30)
    rainbow()
    sky(200)
    sd.pause()
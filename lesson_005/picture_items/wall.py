import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (255, 255, 255)


def wall(start_x, length, height, brick_size):
    for row, y in enumerate(range(0, height, brick_size)):
        x0 = brick_size if row % 2 == 0 else 0
        for x in range(start_x + x0, start_x + length - brick_size, brick_size * 2):
            left_bottom = sd.get_point(x, y)
            right_top = sd.get_point(x + brick_size * 2, y + brick_size)
            sd.rectangle(left_bottom, right_top, (0, 0, 0), width=2)



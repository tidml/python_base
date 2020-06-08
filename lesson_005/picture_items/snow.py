import simple_draw as sd


def snowbank (start_x, size):
    for y in range(0, size, 20):
        for x in range(start_x, start_x + size, 20):
            point = sd.get_point(x, y)
            sd.snowflake(point, 30, sd.COLOR_BLUE)
        start_x += 20
        size -= 40


if __name__ == "__main__":
    sd.resolution = (1200, 600)
    snowbank(200, 210)
    sd.pause()
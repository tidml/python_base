import simple_draw as sd

sd.resolution = (1200, 600)

# Списки параметров
x_list = []
size_list = []
length_list = []


def snowflakes(quantity):
    for _ in range(quantity):
        new_x = sd.random_number(50, 1150)
        x_list.append(new_x)
        new_size = sd.random_number(10, 40)
        size_list.append(new_size)
        new_length = round(sd.random_number(10, 90) / 100, 1)
        length_list.append(new_length)
    for y in range(600, 0, -5):
        sd.clear_screen()
        for i, x in enumerate(x_list):
            point = sd.get_point(x, y)
            sd.snowflake(center=point, length=size_list[i], factor_b=length_list[i])
        sd.sleep(0.1)


snowflakes(5)

sd.pause()

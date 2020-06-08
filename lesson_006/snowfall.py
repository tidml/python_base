import simple_draw as sd

if __name__ == "__main__":
    sd.resolution = (1200, 600)

x_list = []
y_list = []
size_list = []
length_list = []
fallen_snowflakes_list = []


def add_snowflakes(quantity):
    global x_list, y_list, size_list, length_list
    for _ in range(quantity):
        new_x = sd.random_number(50, 1150)
        new_y = sd.random_number(0, 600)
        new_size = sd.random_number(10, 40)
        new_length = round(sd.random_number(10, 90) / 100, 1)
        x_list.append(new_x)
        y_list.append(new_y)
        size_list.append(new_size)
        length_list.append(new_length)


def color_snowflakes(color=sd.COLOR_WHITE):
    global x_list, y_list, size_list
    sd.start_drawing()
    for i, x in enumerate(x_list):
        if y_list[i] <= 0:
            color = sd.background_color
        point = sd.get_point(x_list[i], y_list[i])
        sd.snowflake(center=point, length=size_list[i], color=color, factor_b=length_list[i])
    sd.finish_drawing()


def move_snowflakes():
    global y_list
    for i in range(len(y_list)):
        y_list[i] -= 5


def fallen_snowflakes():
    global fallen_snowflakes_list, x_list
    fallen_snowflakes_list.clear()
    fallen_snowflakes_count = 0
    for i, x in enumerate(x_list):
        if y_list[i] <= 0:
            fallen_snowflakes_list.append(i)
            fallen_snowflakes_count += 1
    return fallen_snowflakes_count


def delete_snowflake():
    global x_list, y_list, size_list, length_list, fallen_snowflakes_list
    for snowflake in reversed(sorted(fallen_snowflakes_list)):
        x_list.pop(snowflake)
        y_list.pop(snowflake)
        size_list.pop(snowflake)
        length_list.pop(snowflake)


# Использовать функции надо в главном модуле
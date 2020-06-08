import simple_draw as sd


def tree(point, angle, length):
    if length < 10:
        return
    branch = sd.get_vector(point, angle, length, 1)
    branch.draw()
    next_point = branch.end_point
    angle_for_right_branch = angle - 30
    angle_for_left_branch = angle + 30
    next_length = length * 0.75
    tree(next_point, angle_for_right_branch, next_length)
    tree(next_point, angle_for_left_branch, next_length)


def random_tree(point, angle, length):
    if length < 10:
        return
    color = sd.COLOR_BLACK
    if length < 30:
        color = sd.COLOR_GREEN
    branch = sd.get_vector(point, angle, length, 2)
    branch.draw(color=color)
    angel_delta = sd.random_number(18, 42)
    length_delta = sd.random_number(60, 90) / 100
    next_point = branch.end_point
    angle_for_right_branch = angle - angel_delta
    angle_for_left_branch = angle + angel_delta
    next_length = length * length_delta
    random_tree(next_point, angle_for_right_branch, next_length)
    random_tree(next_point, angle_for_left_branch, next_length)


def forest(start_x, length, quantity):
    for _ in range(quantity):
        root_point = sd.get_point(start_x, 0)
        random_tree(root_point, angle=90, length=length)
        start_x += 10


if __name__ == "__main__":
    sd.resolution = (1200, 800)
    root_point = sd.get_point(600, 30)
    tree(point=root_point, angle=90, length=200)
    root_point = sd.get_point(600, 0)
    random_tree(root_point, angle=90, length=100)
    sd.pause()
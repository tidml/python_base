# -*- coding: utf-8 -*-

# (if/elif/else)

# Заданы размеры envelop_x, envelop_y - размеры конверта и paper_x, paper_y листа бумаги
#
# Определить, поместится ли бумага в конверте (стороны листа параллельны сторонам конверта)
# Не забывайте, что лист бумаги можно перевернуть и попробовать вставить в конверт другой стороной.
# Результат проверки вывести на консоль (ДА/НЕТ)
# Использовать только операторы if/elif/else, можно вложенные

envelop_x, envelop_y = 10, 7
# paper_x, paper_y = 8, 9
# проверить для
paper_x, paper_y = 9, 8
# paper_x, paper_y = 6, 8
# paper_x, paper_y = 8, 6
# paper_x, paper_y = 3, 4
# paper_x, paper_y = 11, 9
# paper_x, paper_y = 9, 11
# (просто раскоментировать нужную строку и проверить свой код)

def paper_in_envelop():
    envelop_x, envelop_y = 10, 7
    if envelop_x >= paper_x and envelop_y >= paper_y:
        print('Лист бумаги поместился в конверт')
    elif envelop_x >= paper_y and envelop_y >= paper_x:
        print('Лист поместился в конверт, но его пришло перевернуть')
    else:
        print('Лист слишком большой для этого конверта')

paper_in_envelop()

# Усложненное задание, решать по желанию.
# Заданы размеры hole_x, hole_y прямоугольного отверстия и размеры brick_х, brick_у, brick_z кирпича (все размеры
# могут быть в диапазоне от 1 до 1000)
#
# Определить, пройдет ли кирпич через отверстие (грани кирпича параллельны сторонам отверстия)

# hole_x, hole_y = 8, 9
# brick_x, brick_y, brick_z = 11, 10, 2
# brick_x, brick_y, brick_z = 11, 2, 10
# brick_x, brick_y, brick_z = 10, 11, 2
# brick_x, brick_y, brick_z = 10, 2, 11
# brick_x, brick_y, brick_z = 2, 10, 11
# brick_x, brick_y, brick_z = 2, 11, 10
# brick_x, brick_y, brick_z = 3, 5, 6
# brick_x, brick_y, brick_z = 3, 6, 5
# brick_x, brick_y, brick_z = 6, 3, 5
# brick_x, brick_y, brick_z = 6, 5, 3
# brick_x, brick_y, brick_z = 5, 6, 3
# brick_x, brick_y, brick_z = 5, 3, 6
brick_x, brick_y, brick_z = 11, 3, 6
# brick_x, brick_y, brick_z = 11, 6, 3
# brick_x, brick_y, brick_z = 6, 11, 3
# brick_x, brick_y, brick_z = 6, 3, 11
# brick_x, brick_y, brick_z = 3, 6, 11
# brick_x, brick_y, brick_z = 3, 11, 6
# (просто раскоментировать нужную строку и проверить свой код)

def brick_through_the_hole():
    hole_x, hole_y = 8, 9
    # ширина и высота кирпича меньше отверстия
    if hole_x >= brick_x and hole_y >= brick_y:
        print('Кирпич пройдет через отверстие')
    # либо ширина, либо высота кирпича оказались больше соответствующей стороны отверстия
    elif hole_x >= brick_y and hole_y >= brick_x:
        print('Кирпич пройдет через отверстие, но его нужно повернуть по оси Z')
    # одна из сторон оказаласб больше любой стороны отверстия
    else:
        # если ширина кирпича оказалась больше, а высота нет, сравниваем длину кирпича с шириной отверстия
        if hole_x >= brick_z and hole_y >= brick_y:
            print('Кирпич пройдет через отверстие, но его нужно повернуть по оси y')
        # если высота кирпича оказалась больше, а ширина нет, сравниваем длину кирпича с высотой отверстия
        elif hole_x >= brick_x and hole_y >= brick_z:
            print('Кирпич пройдет через отверстие, но его нужно повернуть по оси x')
        # Правки
        elif hole_x >= brick_z and hole_y >= brick_x:
            print('Кирпич пройдет через отверстие, но его нужно повернуть по оси x')
        # Правки
        elif hole_x >= brick_y and hole_y >= brick_z:
            print('Кирпич пройдет через отверстие, но его нужно повернуть по оси y')
        else:
            print('Кирпич слишком большой для данного отверстия')


brick_through_the_hole()

#зачет!
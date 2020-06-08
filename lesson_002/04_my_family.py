#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создайте списки:

# моя семья (минимум 3 элемента, есть еще дедушки и бабушки, если что)
my_family = ['Мама', 'Папа', 'Брат']

mom = [my_family[0], 165]
dad = [my_family[1], 175]
bro = [my_family[2], 181]

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    mom,
    dad,
    bro
]

# Выведите на консоль рост отца в формате
#   Рост отца - ХХ см

print('Рост отца - ', my_family_height[1][1], 'см')

# Выведите на консоль общий рост вашей семьи как сумму ростов всех членов
#   Общий рост моей семьи - ХХ см

mom_height = my_family_height[0][1]
dad_height = my_family_height[1][1]
bro_height = my_family_height[2][1]

print('Общий рост моей семьи - ', mom_height + dad_height + bro_height, ' см')


#зачет!
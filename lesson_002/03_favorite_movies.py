#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

from pprint import pprint

first_film = my_favorite_movies[0:10]
last_film = my_favorite_movies[-15:-1]
second_film = my_favorite_movies[12:25]
penultimate_film = my_favorite_movies[-22:-17]

print(first_film, last_film, second_film, penultimate_film, sep="\n")

#зачет!

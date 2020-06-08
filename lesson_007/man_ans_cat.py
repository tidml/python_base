# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.





# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# До этого изменения внес в файл practice

if __name__ == "__main__":

    from python_snippets.practice import House


    class Man:

        def __init__(self, name):
            self.name = name
            self.fullness = 100
            self.house = None
            self.cat = None

        def __str__(self):
            return 'Я - {}, сытость {}, живу {}'.format(
                self.name, self.fullness, self.house)

        def eat(self):
            if self.house.food >= 10:
                cprint('{} поел'.format(self.name), color='yellow')
                self.fullness += 10
                self.house.food -= 10
            else:
                cprint('{} нет еды'.format(self.name), color='red')

        def work(self):
            cprint('{} сходил на работу'.format(self.name), color='blue')
            self.house.money += 150
            self.fullness -= 10

        def go_to_gym(self):
            cprint('{} тренировался целый день'.format(self.name), color='green')
            self.fullness -= 10

        def shopping(self):
            if self.house.money >= 50:
                cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
                self.house.money -= 50
                self.house.food += 50
            else:
                cprint('{} деньги кончились!'.format(self.name), color='red')

        def go_to_the_house(self, house):
            self.house = house
            self.fullness -= 10
            cprint('{} Вьехал в дом'.format(self.name), color='cyan')

        def pick_up_a_cat(self, cat, house):
            self.cat = cat
            self.cat.house = house
            cprint('{} теперь будет жить с нами'.format(self.cat.name), color='cyan')

        def buy_cats_food(self):
            if self.house.money >= 50:
                cprint('Купил еды. {} не останется голодной'.format(self.cat.name), color='magenta')
                self.house.money -= 50
                self.house.cats_food += 50
            else:
                cprint('{} деньги кончились!'.format(self.name), color='red')

        def clean_the_house(self):
            if self.house.dirt >= 100:
                cprint('{} убрался дома'.format(self.name), color='blue')
                self.house.dirt -= 100
                self.fullness -= 20

        def act(self):
            if self.fullness <= 0:
                cprint('{} умер...'.format(self.name), color='red')
                return False
            dice = randint(1, 6)
            if self.fullness < 40:
                self.eat()
            elif self.house.food < 20:
                self.shopping()
            elif self.house.cats_food < 20:
                self.buy_cats_food()
            elif self.house.money < 50:
                self.work()
            elif self.house.dirt >= 100:
                self.clean_the_house()
            elif dice == 1:
                self.work()
            elif dice == 2:
                self.eat()
            else:
                self.go_to_gym()


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def __str__(self):
        return 'Кошка {}, сытость {}'.format(self.name, self.fullness)

    def sleep(self):
        cprint('{} поспала'.format(self.name), color='yellow')
        self.fullness -= 10

    def eat(self):
        if self.house.cats_food >= 10:
            cprint('{} поела'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.cats_food -= 5
        else:
            self.fullness -= 10
            cprint('{} без еды'.format(self.name), color='red')

    def tearing_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='red')
        self.fullness -= 10
        self.house.dirt += 5

    def act(self):
        if self.fullness <= 0:
            cprint('{} умерла Т.Т'.format(self.name), color='red')
            return False
        choose_activity = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif choose_activity == 1:
            self.tearing_wallpaper()
        else:
            self.sleep()


if __name__== "__main__":
    my_cat = Cat('Мурка')
    me = Man('Никита')
    my_home = House()

    me.pick_up_a_cat(my_cat, my_home)
    me.go_to_the_house(my_home)

    for day in range(1, 366):
        print('================ день {} =================='.format(day))
        me.act()
        my_cat.act()
        print('--- в конце дня ---')
        print(me, my_cat, sep='\n')

# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
#Зачет!
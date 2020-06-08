# -*- coding: utf-8 -*-

from random import randint


# Реализуем модель человека.
# Человек может есть, работать, играть, ходить в магазин.
# У человека есть степень сытости, немного еды и денег.
# Если сытость < 0 единиц, человек умирает.
# Человеку надо прожить 365 дней.
from termcolor import cprint


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

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
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
            return
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
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cats_food = 0
        self.dirt = 0

    def __str__(self):
        return 'в доме: еды осталось {}, денег осталось {}'.format(
            self.food, self.money)


if __name__ == "__main__":
    citizens = [
        Man(name='Бивис'),
        Man(name='Батхед'),
        Man(name='Кенни'),
    ]

    my_sweet_home = House()
    for citizen in citizens:
        citizen.go_to_the_house(house=my_sweet_home)

    for day in range(1, 366):
        print('================ день {} =================='.format(day))
        for citizen in citizens:
            citizen.act()
        print('--- в конце дня ---')
        for citizen in citizens:
            print(citizen)
        print(my_sweet_home)

# Создадим двух людей, живущих в одном доме - Бивиса и Батхеда
# Нужен класс Дом, в нем должн быть холодильник с едой и тумбочка с деньгами
# Еда пусть хранится в холодильнике в доме, а деньги - в тумбочке.

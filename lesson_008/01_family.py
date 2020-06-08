# -*- coding: utf-8 -*-


######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умрает от депресии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.
from termcolor import cprint
from random import randint
from man_ans_cat import Cat


class House:

    def __init__(self):
        self.money = 100
        self.food = 50
        self.cats_food = 30
        self.dirt = 0

    def __str__(self):
        return 'В доме денег {}, обычной еды {}, еды для кошки {}, грязи {} '.format(
            self.money, self.food, self.cats_food, self.dirt)


class Human:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.house = None
        self.cat = None

    def __str__(self):
        return '{}, сытость {}, счастье {} '.format(self.name, self.fullness, self.happiness)

    def eat(self, portion=30):
        if self.fullness >= 100:
            print(f'{self.name} не голодный')
            return False
        elif self.house.food <= 0:
            self.fullness -= 10
            cprint('В доме не осталось еды', color='yellow')
            return False
        elif self.house.food < portion:
            self.fullness += self.house.food
            cprint('{} съел(-a) {} еды'.format(self.name, self.house.food), color='yellow')
        else:
            cprint('{} поел(-a)'.format(self.name), color='yellow')
            self.fullness += portion
            self.house.food -= portion

    def pick_up_a_cat(self, cat, house):
        self.cat = cat
        self.cat.house = house
        cprint('{} теперь будет жить с нами'.format(self.cat.name), color='cyan')

    def pat_the_cat(self):
        if self.cat.fullness <= 0:
            cprint(f'Некого гладить. {self.cat.name} умерла', color='red')
        else:
            self.fullness -= 10
            self.happiness += 5
            print(f'{self.name} гладит {self.cat.name}')

    def buy_cats_food(self):
        if self.house.money >= 50:
            cprint('{} купил(а) еды. {} не останется голодной'.format(self.name, self.cat.name), color='magenta')
            self.fullness -= 10
            self.house.money -= 50
            self.house.cats_food += 50
        else:
            cprint('{} останется без еды, деньги кончились!'.format(self.cat.name), color='red')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер от голода...'.format(self.name), color='red')
            return False
        elif self.happiness <= 0:
            cprint('{} умер от депрессии...'.format(self.name), color='red')
            return False
        elif self.fullness <= 20:
            self.eat()
            return False
        else:
            return True

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')


class Husband(Human):

    def work(self):
        if self.house.money >= 1000:
            cprint('{} остается дома. В доме достаточно денег'.format(self.name), color='yellow')
            return False
        self.fullness -= 10
        self.happiness -= 10
        self.house.money += 150
        cprint('{} сходил на работу'.format(self.name), color='blue')

    def gaming(self):
        self.fullness -= 10
        self.happiness += 20
        cprint('{} поиграл в WoT'.format(self.name), color='green')

    def act(self):
        if super().act():
            if self.house.dirt >= 70:
                self.happiness -= 10
            choose_activity = randint(1, 6)
            if self.happiness >= 100:
                self.work()
            elif self.happiness <= 10:
                self.gaming()
            elif self.house.cats_food <= 20:
                self.buy_cats_food()
            elif self.house.money <= 50:
                self.work()
            elif choose_activity == 1:
                self.gaming()
            elif choose_activity in range(2, 4):
                self.pat_the_cat()
            else:
                self.work()


class Wife(Human):

    def shopping(self):
        if self.house.money <= 10:
            cprint('В доме закончились деньги', color='red')
            return False
        elif self.house.money <= 50:
            self.house.food += self.house.money
            self.house.money -= self.house.money
            cprint('{} купила домой {} продуктов'.format(self.name, self.house.food), color='blue')
        elif self.house.food >= 120:
            cprint('В доме достаточно еды', color='yellow')
            return False
        else:
            self.house.money -= 60
            self.house.food += 60
            cprint('{} купила домой еды'.format(self.name), color='blue')

    def buy_fur_coat(self):
        if self.house.money >= 350:
            self.fullness -= 10
            self.happiness += 20
            self.house.money -= 350
            cprint('{} купила шубу'.format(self.name), color='green')
        else:
            cprint('{} хотела шубу, но не хватает денег'.format(self.name), color='green')

    def clean_house(self):
        self.fullness -= 10
        self.house.dirt -= 100
        cprint('{} убралась дома'.format(self.name), color='blue')

    def watching_tv(self):
        self.fullness -= 10
        self.happiness += 10
        cprint('{} смотрит телевизор'.format(self.name), color='green')

    def act(self):
        if super().act():
            if self.house.dirt >= 70:
                self.happiness -= 10
            choose_activity = randint(1, 6)
            if self.house.dirt >= 100:
                self.clean_house()
            elif self.happiness >= 100:
                self.shopping()
            elif self.house.cats_food <= 20:
                self.buy_cats_food()
            elif self.house.food <= 50:
                self.shopping()
            elif self.happiness <= 20:
                self.watching_tv()
            elif choose_activity == 1:
                self.shopping()
            elif choose_activity == 2:
                self.buy_fur_coat()
            else:
                self.pat_the_cat()


class Child(Human):

    def __str__(self):
        return super().__str__()

    def eat(self, portion=10):  # При переопределении параметры должны быть такими же, как в родителе
        super().eat(portion=10)

    def sleep(self):
        self.fullness -= 10
        cprint('{} поспал'.format(self.name), color='green')

    def act(self):
        if super().act():
            choose_activity = randint(1, 6)
            if choose_activity in range(1, 3):
                self.sleep()
            else:
                self.eat()


home = House()
serge = Husband(name='Сережа')
masha = Wife(name='Маша')
kolya = Child(name='Коля')
murka = Cat(name='Мурка')
serge.go_to_the_house(home)
masha.go_to_the_house(home)
kolya.go_to_the_house(home)
serge.pick_up_a_cat(cat=murka, house=home)
masha.pick_up_a_cat(cat=murka, house=home)

for day in range(365):
    home.dirt += 5
    cprint('================== День {} =================='.format(day), color='red')
    serge.act()
    masha.act()
    murka.act()
    kolya.act()
    cprint(serge, color='cyan')
    cprint(masha, color='cyan')
    cprint(murka, color='cyan')
    cprint(kolya, color='yellow')
    print(home)

######################################################## Часть вторая
#
# После подтверждения учителем первой части надо
# отщепить ветку develop и в ней начать добавлять котов в модель семьи
#
# Кот может:
#   есть,
#   спать,
#   драть обои
#
# Люди могут:
#   гладить кота (растет степень счастья на 5 пунктов)
#
# В доме добавляется:
#   еда для кота (в начале - 30)
#
# У кота есть имя и степень сытости (в начале - 30)
# Любое действие кота, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Еда для кота покупается за деньги: за 10 денег 10 еды.
# Кушает кот максимум по 10 единиц еды, степень сытости растет на 2 пункта за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе кот умрет от голода.
#
# Если кот дерет обои, то грязи становится больше на 5 пунктов


# class Cat:
#
#     def __init__(self):
#         pass
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#     def soil(self):
#         pass


######################################################## Часть вторая бис
#
# После реализации первой части надо в ветке мастер продолжить работу над семьей - добавить ребенка
#
# Ребенок может:
#   есть,
#   спать,
#
# отличия от взрослых - кушает максимум 10 единиц еды,
# степень счастья  - не меняется, всегда ==100 ;)

# class Child:
#
#     def __init__(self):
#         pass
#
#     def __str__(self):
#         return super().__str__()
#
#     def act(self):
#         pass
#
#     def eat(self):
#         pass
#
#     def sleep(self):
#         pass
#
#


######################################################## Часть третья
#
# после подтверждения учителем второй части (обоих веток)
# влить в мастер все коммиты из ветки develop и разрешить все конфликты
# отправить на проверку учителем.


# home = House()
# serge = Husband(name='Сережа')
# masha = Wife(name='Маша')
# kolya = Child(name='Коля')
# murzik = Cat(name='Мурзик')
#
# for day in range(365):
#     cprint('================== День {} =================='.format(day), color='red')
#     serge.act()
#     masha.act()
#     kolya.act()
#     murzik.act()
#     cprint(serge, color='cyan')
#     cprint(masha, color='cyan')
#     cprint(kolya, color='cyan')
#     cprint(murzik, color='cyan')


# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# Дополнительно вносить некий хаос в жизнь семьи
# - N раз в год вдруг пропадает половина еды из холодильника (коты?)
# - K раз в год пропадает половина денег из тумбочки (муж? жена? коты?!?!)
# Промоделировать - как часто могут случаться фейлы что бы это не повлияло на жизнь героев?
#   (N от 1 до 5, K от 1 до 5 - нужно вычислит максимумы N и K при котором семья гарантированно выживает)
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
#зачет!
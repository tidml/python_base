# -*- coding: utf-8 -*-

# Подземелье было выкопано ящеро-подобными монстрами рядом с аномальной рекой, постоянно выходящей из берегов.
# Из-за этого подземелье регулярно затапливается, монстры выживают, но не герои, рискнувшие спуститься к ним в поисках
# приключений.
# Почуяв безнаказанность, ящеры начали совершать набеги на ближайшие деревни. На защиту всех деревень не хватило
# солдат и вас, как известного в этих краях героя, наняли для их спасения.
#
# Карта подземелья представляет собой json-файл под названием rpg.json. Каждая локация в лабиринте описывается объектом,
# в котором находится единственный ключ с названием, соответствующем формату "Location_<N>_tm<T>",
# где N - это номер локации (целое число), а T (вещественное число) - это время,
# которое необходимо для перехода в эту локацию. Например, если игрок заходит в локацию "Location_8_tm30000",
# то он тратит на это 30000 секунд.
# По данному ключу находится список, который содержит в себе строки с описанием монстров а также другие локации.
# Описание монстра представляет собой строку в формате "Mob_exp<K>_tm<M>", где K (целое число) - это количество опыта,
# которое получает игрок, уничтожив данного монстра, а M (вещественное число) - это время,
# которое потратит игрок для уничтожения данного монстра.
# Например, уничтожив монстра "Boss_exp10_tm20", игрок потратит 20 секунд и получит 10 единиц опыта.
# Гарантируется, что в начале пути будет две локации и один монстр
# (то есть в коренном json-объекте содержится список, содержащий два json-объекта, одного монстра и ничего больше).
#
# На прохождение игры игроку дается 123456.0987654321 секунд.
# Цель игры: за отведенное время найти выход ("Hatch")
#
# По мере прохождения вглубь подземелья, оно начинает затапливаться, поэтому
# в каждую локацию можно попасть только один раз,
# и выйти из нее нельзя (то есть двигаться можно только вперед).
#
# Чтобы открыть люк ("Hatch") и выбраться через него на поверхность, нужно иметь не менее 280 очков опыта.
# Если до открытия люка время заканчивается - герой задыхается и умирает, воскрешаясь перед входом в подземелье,
# готовый к следующей попытке (игра начинается заново).
#
# Гарантируется, что искомый путь только один, и будьте аккуратны в рассчетах!
# При неправильном использовании библиотеки decimal человек, играющий с вашим скриптом рискует никогда не найти путь.
#
# Также, при каждом ходе игрока ваш скрипт должен запоминать следущую информацию:
# - текущую локацию
# - текущее количество опыта
# - текущие дату и время (для этого используйте библиотеку datetime)
# После успешного или неуспешного завершения игры вам необходимо записать
# всю собранную информацию в csv файл dungeon.csv.
# Названия столбцов для csv файла: current_location, current_experience, current_date
#
#
# Пример взаимодействия с игроком:
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло времени: 00:00
#
# Внутри вы видите:
# — Вход в локацию: Location_1_tm1040
# — Вход в локацию: Location_2_tm123456
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали переход в локацию Location_2_tm1234567890
#
# Вы находитесь в Location_2_tm1234567890
# У вас 0 опыта и осталось 0.0987654321 секунд до наводнения
# Прошло времени: 20:00
#
# Внутри вы видите:
# — Монстра Mob_exp10_tm10
# — Вход в локацию: Location_3_tm55500
# — Вход в локацию: Location_4_tm66600
# Выберите действие:
# 1.Атаковать монстра
# 2.Перейти в другую локацию
# 3.Сдаться и выйти из игры
#
# Вы выбрали сражаться с монстром
#
# Вы находитесь в Location_2_tm0
# У вас 10 опыта и осталось -9.9012345679 секунд до наводнения
#
# Вы не успели открыть люк!!! НАВОДНЕНИЕ!!! Алярм!
#
# У вас темнеет в глазах... прощай, принцесса...
# Но что это?! Вы воскресли у входа в пещеру... Не зря матушка дала вам оберег :)
# Ну, на этот-то раз у вас все получится! Трепещите, монстры!
# Вы осторожно входите в пещеру... (текст умирания/воскрешения можно придумать свой ;)
#
# Вы находитесь в Location_0_tm0
# У вас 0 опыта и осталось 123456.0987654321 секунд до наводнения
# Прошло уже 0:00:00
# Внутри вы видите:
#  ...
#  ...
#
# и так далее...
import csv
import datetime
import json
import re
from decimal import *


class Rpg:

    def __init__(self, json_file):
        self.json_file = json_file
        self.dictionary = None
        self.options_for_action = []
        self.experience = 0
        self.remaining_time = Decimal('123456.0987654321')
        self.current_time = datetime.datetime.now()
        self.re_time = r'\w+\d*_tm(\d+\.?\d*)'
        self.re_location = r'Location_(\w*\d+)_tm(\d+)'
        self.day = self.current_time.strftime("_%d_%m")
        self.game_count = 0

    def json_processing(self):
        with open(self.json_file, 'r', encoding='utf8') as json_data:
            self.dictionary = json.load(json_data)

    def create_csv(self):
        fields_names = ['current_location', 'current_experience', 'current_date']
        with open(f'dungeon{self.game_count}{self.day}.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            writer.writerow(fields_names)

    def choose_action(self, data):
        print(f"\nУ вас осталось времени {self.remaining_time}")
        print(f'Ваш текущий уровень уровень {self.experience}\n')
        print('Выберите действие:')
        for number, option in enumerate(data):
            if isinstance(option, dict):
                y = str(*option.keys())
                print(f'{number}. Перейти в {y}')
            else:
                print(f'{number}. Убить {option}')

    def show_options(self, dictionary):
        for key, data in dictionary.items():
            location = re.search(self.re_location, key)
            print(f'\nВы находитесь в Локации {location[1]}', f'Время ее прохождения {location[2]}', sep='\n')
            print('Внутри вы видите:')
            for number, option in enumerate(data):
                if isinstance(option, dict):
                    y = str(*option.keys())
                    print(f'- {y}')
                else:
                    print(f'- {option}')
                self.options_for_action.append(option)
            self.choose_action(data)

    def counting_experience_points(self, choice):
        re_monster = r'Mob_exp(\d+)_tm(\d+)'
        re_boss = r'Boss\d*_exp(\d+)_tm(\d+)'
        monster = re.search(re_monster, choice)
        boss = re.search(re_boss, choice)
        if boss is not None:
            exp = boss[1]
        else:
            exp = monster[1]
        self.experience += int(exp)

    def countdown(self, choice):
        time = re.search(self.re_time, choice)
        time_spent = Decimal(time[1])
        self.remaining_time -= time_spent

    def writing_in_csv(self, choice):
        with open(f'dungeon{self.game_count}{self.day}.csv', 'a', newline='') as out_csv:
            writer = csv.writer(out_csv)
            location = re.search(self.re_location, choice)
            if choice == 'Hatch_tm159.098765432':
                data = [choice, self.experience, self.current_time.strftime("%d.%m.%y")]
            else:
                data = [f'Location {location[1]}', self.experience, self.current_time.strftime("%d.%m.%y")]
            writer.writerow(data)
            data.clear()

    def input_validation(self, user_input):
        number_of_options = len(self.options_for_action)
        while len(user_input) != 1 or ord(user_input) not in range(48, 58) \
                or int(user_input) not in range(number_of_options):
            print(f'Вы ввели неверное значение! Введите число, от 0 до {number_of_options - 1}')
            user_input = input('Ваш выбор: ')
        return int(user_input)

    def game(self):
        if len(self.options_for_action) == 0:
            print('===== Вы проиграли =====',
                  'Вы зашли в тупик, выхода нету =(',
                  f'Пещеру затопило...', sep='\n')
            return False
        user_input = input('Ваш выбор: ')
        user_input = self.input_validation(user_input)
        choice = self.options_for_action[user_input]
        if isinstance(choice, dict):
            user_choice = str(*choice.keys())
            if user_choice == 'Hatch_tm159.098765432':
                self.countdown(user_choice)
                if self.experience >= 280 and self.remaining_time > 0:
                    print('===== Победа! =====')
                    print(f'Оставшееся время {self.remaining_time.quantize(Decimal("1.000"), ROUND_HALF_EVEN)}, '
                          f'Полученный опыт {self.experience}')
                elif len(self.options_for_action) > 1:
                    print('Недостаточно опыта, чтобы войти',
                          f'Необходимо 280, а ваш текущий уровень {self.experience}', sep='\n')
                    return True
                else:
                    print('===== Вы проиграли =====',
                          f'Ваш текущий уровень {self.experience}',
                          f'Оставшееся время {self.remaining_time}', sep='\n')
                self.writing_in_csv(user_choice)
                return False
            self.writing_in_csv(user_choice)
            self.countdown(user_choice)
            self.show_options(choice)
            self.options_for_action = list(*choice.values())
        else:
            self.countdown(choice)
            self.counting_experience_points(choice)
            self.options_for_action.pop(user_input)
            self.choose_action(self.options_for_action)
        return True

    def run(self):
        new_game = 'yes'
        while new_game == 'yes':
            self.create_csv()
            self.json_processing()
            self.remaining_time = Decimal('123456.0987654321')
            self.options_for_action = []
            self.experience = 0
            self.show_options(self.dictionary)
            x = True
            while x is True:
                x = self.game()
            else:
                self.game_count += 1
                print('Хотите начать новую игру?')
                new_game = input('Yes / No: ').lower()


rpg_json = 'rpg.json'
game = Rpg(rpg_json)
game.run()

# Учитывая время и опыт, не забывайте о точности вычислений!
#зачет!
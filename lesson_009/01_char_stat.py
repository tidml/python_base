

# -*- coding: utf-8 -*-

# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

import zipfile
from operator import itemgetter


class LetterCounter:

    def __init__(self, zip_file_name):
        self.zip_file_name = zip_file_name
        self.file_name = None
        self.stat = {}
        self.sort = None

    def run(self):
        self.unzip()
        self.count_letters()
        self.sort_data()
        self.output_data()

    def unzip(self):
        zfile = zipfile.ZipFile(self.zip_file_name, 'r')
        for file_name in zfile.namelist():
            zfile.extract(file_name)
        self.file_name = file_name

    def count_letters(self):
        with open(self.file_name, 'r', encoding='ANSI') as file:
            for line in file:
                for letter in line:
                    if letter.isalpha():
                        if letter in self.stat:
                            self.stat[letter] += 1
                        else:
                            self.stat[letter] = 1

    def sort_data(self):
        pass

    def output_data(self):
        total_count = 0
        print(f'| {"буква":^8} | {"частота":^8} |')
        for letter, count in self.sort:
            print(f'+{"+":-^21}+')
            print(f'| {letter:^8} | {count:^8} |')
            total_count += count
        print(f'+{"+":-^21}+')
        print(f'| {"Итого":^8} | {total_count:^8} |')


class ReverseAlphabeticalOrder(LetterCounter):

    def sort_data(self):
        self.sort = sorted(self.stat.items(), reverse=True)


class AlphabeticalOrder(LetterCounter):

    def sort_data(self):
        self.sort = sorted(self.stat.items(), reverse=False)


class DecreasingOrder(LetterCounter):

    def sort_data(self):
        self.sort = sorted(self.stat.items(), key=itemgetter(1), reverse=True)


class IncreasingOrder(LetterCounter):

    def sort_data(self):
        self.sort = sorted(self.stat.items(), key=itemgetter(1), reverse=False)


zip_file_name = 'voyna-i-mir.txt.zip'

counter = DecreasingOrder(zip_file_name)
counter.run()


# После выполнения первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://goo.gl/Vz4828
#   и пример https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4
#Зачет!
# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.


class StatusCounter:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.HOUR = slice(1, 14)
        self.DAY = slice(1, 11)
        self.MINUTE = slice(1, 17)
        self.STATUS = slice(29, 32)

    def run(self, out_file_name=None):
        self.group_count()
        self.output_data(out_file_name)

    def group_count(self):
        pass

    def count(self, user_input):
        with open(self.file_name, 'r', encoding='utf8') as file:
            for line in file:
                user_date = line[user_input]
                status = line[29:32]
                if status == 'NOK':
                    if user_date in self.stat:
                        self.stat[user_date] += 1
                    else:
                        self.stat[user_date] = 1

    def output_data(self, out_file_name=None):
        if out_file_name is not None:
            file = open(out_file_name, 'w', encoding='utf8')
        else:
            file = None
            for user_date, count in self.stat.items():
                if file:
                    file.write(f'[{user_date}] {count} \n')
                else:
                    print(f'[{user_date}] {count}')


class DayStatusCounter(StatusCounter):

    def group_count(self):
        self.count(self.DAY)


class HourStatusCounter(StatusCounter):

    def group_count(self):
        self.count(self.HOUR)


class MinuteStatusCounter(StatusCounter):

    def group_count(self):
        self.count(self.MINUTE)


file_name = 'events.txt'
out_file_name = 'out_data.txt'
counter = MinuteStatusCounter(file_name)
counter.run()
counter = HourStatusCounter(file_name)
counter.run()
counter = DayStatusCounter(file_name)
counter.run()
# После выполнения первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!
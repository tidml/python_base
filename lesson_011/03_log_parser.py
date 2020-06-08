# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


def count(file_name):
    with open(file_name, 'r', encoding='utf8') as file:
        current_date = set()
        count = 0
        for line in file:
            minute, status = line[1:17], line[29:32]
            if minute in current_date:
                if status == 'NOK':
                    count += 1
            else:
                if len(current_date) != 0:
                    yield str(*current_date), count
                    count = 1 if status == 'NOK' else 0
                    current_date.clear()
                current_date.add(minute)


file_name = 'events.txt'
grouped_events = count(file_name)
for minute, count in grouped_events:
    print(f'[{minute}] {count}')
#зачет!
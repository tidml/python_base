# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru


from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse


class MakeTicket:

    def __init__(self, fio, from_, to, date, font='tahoma.ttf', path='images/ticket_template.png'):
        self.data_list = [fio, from_, to, date]
        self.font = ImageFont.truetype(font, size=16)
        self.ticket = Image.open(path)
        self.completed_ticket = ImageDraw.Draw(self.ticket)

    def make_ticket(self, out_path=None):
        step = 0
        for data in self.data_list[:-1]:
            self.completed_ticket.rectangle((45, 125 + step, 230, 141 + step), fill='white')
            self.completed_ticket.text((45, 125 + step), data, font=self.font, fill=ImageColor.colormap['black'])
            step += 70
        self.completed_ticket.rectangle((290, 265, 350, 281), fill='white')
        self.completed_ticket.text((290, 265), self.data_list[-1], font=self.font, fill=ImageColor.colormap['black'])
        out_path = out_path if out_path else 'user_ticket.png'
        self.ticket.save(out_path)


if __name__ == '__main__':
    # fio = 'Тищенко Никита Михайлович'
    # from_ = 'Сургут'
    # to = 'Москва'
    # date = '01.21'
    parser = argparse.ArgumentParser(description='User data for Skillbox AirLine ticket')
    parser.add_argument('-f', '--fio', type=str, help='Users name')
    parser.add_argument('-fr', '--from_', type=str, help='The place of departure')
    parser.add_argument('-t', '--to', type=str, help='The place of arrival')
    parser.add_argument('-d', '--date', type=str, help='THe date of departure')
    args = parser.parse_args()
    maker = MakeTicket(args.fio, args.from_, args.to, args.date)
    maker.make_ticket()
    # python 01_ticket.py -f "Тищенко Никита Михайлович" -fr Сургут -t Москва -d 01.21

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
#зачет!
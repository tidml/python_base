# -*- coding: utf-8 -*-

# В очередной спешке, проверив приложение с прогнозом погоды, вы выбежали
# навстречу ревью вашего кода, которое ожидало вас в офисе.
# И тут же день стал хуже - вместо обещанной облачности вас встретил ливень.

# Вы промокли, настроение было испорчено, и на ревью вы уже пришли не в духе.
# В итоге такого сокрушительного дня вы решили написать свою программу для прогноза погоды
# из источника, которому вы доверяете.

# Для этого вам нужно:

# Создать модуль-движок с классом WeatherMaker, необходимым для получения и формирования предсказаний.
# В нём должен быть метод, получающий прогноз с выбранного вами сайта (парсинг + re) за некоторый диапазон дат,
# а затем, получив данные, сформировать их в словарь {погода: Облачная, температура: 10, дата:datetime...}

# Добавить класс ImageMaker.
# Снабдить его методом рисования открытки
# (использовать OpenCV, в качестве заготовки брать lesson_016/python_snippets/external_data/probe.jpg):
#   С текстом, состоящим из полученных данных (пригодится cv2.putText)
#   С изображением, соответствующим типу погоды
# (хранятся в lesson_016/python_snippets/external_data/weather_img ,но можно нарисовать/добавить свои)
#   В качестве фона добавить градиент цвета, отражающего тип погоды
# Солнечно - от желтого к белому
# Дождь - от синего к белому
# Снег - от голубого к белому
# Облачно - от серого к белому

# Добавить класс DatabaseUpdater с методами:
#   Получающим данные из базы данных за указанный диапазон дат.
#   Сохраняющим прогнозы в базу данных (использовать peewee)

# Сделать программу с консольным интерфейсом, постаравшись все выполняемые действия вынести в отдельные функции.
# Среди действий, доступных пользователю, должны быть:
#   Добавление прогнозов за диапазон дат в базу данных
#   Получение прогнозов за диапазон дат из базы
#   Создание открыток из полученных прогнозов
#   Выведение полученных прогнозов на консоль
# При старте консольная утилита должна загружать прогнозы за прошедшую неделю.

# Рекомендации:
# Можно создать отдельный модуль для инициализирования базы данных.
# Как далее использовать эту базу данных в движке:
# Передавать DatabaseUpdater url-путь
# https://peewee.readthedocs.io/en/latest/peewee/playhouse.html#db-url
# Приконнектится по полученному url-пути к базе данных
# Инициализировать её через DatabaseProxy()
# https://peewee.readthedocs.io/en/latest/peewee/database.html#dynamically-defining-a-database
import argparse
import re
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import requests
import cv2
from PIL import Image, ImageDraw, ImageFont
from database import Weather, DatabaseUpdater


class WeatherMaker:

    def __init__(self, url):
        self.url = url
        self.tags_list = None
        self.weather_forecast = {}

    def get_weather_forecast_data(self):
        html = requests.get(self.url)
        html_doc = BeautifulSoup(html.text, features='html.parser')
        self.tags_list = html_doc.find_all('div', {'class': 'forecast-briefly__day'})

    def get_date(self, date_tag):
        datetime = date_tag.get('datetime').split()
        date = datetime[0]
        return date

    def collect_data(self):
        for weather_card in self.tags_list:
            date_tag = weather_card.find('time', {'class': 'time forecast-briefly__date'})
            date = self.get_date(date_tag)
            icon_tag = weather_card.find('img', {'class': 'icon'}).get('src').split('/')[-1]
            icon_name = re.search(r'(\w+\W*\w*).svg', icon_tag)[1]
            icon = f'icons/{icon_name}.png'
            day_temp = weather_card.find('div',
                                         {'class': 'temp forecast-briefly__temp forecast-briefly__temp_day'}).text
            day_temp_value = re.search(r'\w(\+\d*)', day_temp)[1]
            night_temp = weather_card.find('div',
                                           {'class': 'temp forecast-briefly__temp forecast-briefly__temp_night'}).text
            night_temp_value = re.search(r'\w(\+\d*)', night_temp)[1]
            condition = weather_card.find('div', {'class': 'forecast-briefly__condition'}).text
            self.weather_forecast[date] = {'icon': icon, 'day': day_temp_value, 'night': night_temp_value,
                                           'condition': condition}

    def run(self):
        self.get_weather_forecast_data()
        self.collect_data()


class WeatherForecastCard:

    def __init__(self, data, base):
        self.data = data
        self.base = base
        self.icon_path = None
        self.day_temp = None
        self.night_temp = None
        self.condition = None
        self.new_card_path = None

    def draw_gradient(self, color, url, date):
        image = cv2.imread(url)
        height, width, channels = image.shape
        new_card = image.copy()
        thickness = height // 255
        y = height
        b = color[0]
        g = color[1]
        r = color[2]
        for _ in range(0, 255):
            cv2.line(new_card, (0, y), (width, y), (b, g, r), thickness)
            g += 1 if g != 255 else 0
            b += 1 if b != 255 else 0
            r += 1 if r != 255 else 0
            y -= thickness
        self.new_card_path = f'weather_cards/{date}.png'
        cv2.imwrite(self.new_card_path, new_card)

    def make_final_card(self, date):
        data = self.data[date]
        self.icon_path = data['icon']
        self.day_temp = data['day']
        self.night_temp = data['night']
        self.condition = data['condition']
        if self.condition == 'Небольшой дождь' or self.condition == 'Дождь':
            color = (255, 226, 166)
        elif self.condition == 'Облачно с прояснениями' or self.condition == 'Пасмурно':
            color = (170, 170, 170)
        elif self.condition == 'Ясно':
            color = (160, 250, 250)
        else:
            color = (255, 255, 255)
        self.draw_gradient(color, self.base, date)
        card = Image.open(self.new_card_path)
        icon = Image.open(self.icon_path)
        card.paste(icon, (25, 25), mask=icon)
        final_card = ImageDraw.Draw(card)
        header_text = f'{date}\n{self.condition}'
        header_font = ImageFont.truetype("arial.ttf", size=15)
        body_text = f'Погода днем {self.day_temp}\n\nПогода ночью {self.night_temp}'
        body_font = ImageFont.truetype("arialbd.ttf", size=18)
        final_card.text((125, 35), text=header_text, font=header_font, fill=(153, 153, 153))
        final_card.text((25, 160), text=body_text, font=body_font, fill=(41, 44, 51))
        card.save(self.new_card_path)
        print(f'Карточка находится в: {self.new_card_path}')

    def run(self, date):
        self.make_final_card(date)


class WeatherForecastPresenter:

    def __init__(self, data):
        self.data = data

    def show_weather_forecast(self, date):
        data = self.data[date]
        condition = data['condition']
        day = data['day']
        night = data['night']
        print(f'{date}\n'
              f'{condition}\n'
              f'{"-" * 20}\n'
              f'{"Температура днем:":<20}{day}\n'
              f'{"Температура ночью:":<20}{night}\n')

    def week_weather_forecast(self):
        date = datetime.today().date()
        for _ in range(7):
            self.show_weather_forecast(str(date))
            date += timedelta(days=1)


def call_func_in_dates_range(func, data, start_date, end_date):
    for date in data:
        if date > end_date:
            break
        elif date >= start_date:
            func(date)
        else:
            continue


if __name__ == '__main__':
    url_yandex_pogoda = 'https://yandex.ru/pogoda/surgut?via=srp&lat=61.262842&lon=73.399841'
    data = WeatherMaker(url_yandex_pogoda)
    data.run()
    weather_forecast = data.weather_forecast
    current_date = str(datetime.today().date())
    parser = argparse.ArgumentParser(description=
                                     'week_weather_forecast - shows weather forecast for the next week, '
                                     'show_weather_forecast - shows weather forecast for users date, '
                                     'make_card - makes card (date.png) with data from weather forecast for users date,'
                                     'update_database - writes users date and weather forecast for this date in '
                                     'database "Weather",'
                                     'extract_data - shows data from database "Weather" by users date')
    parser.add_argument('-d', '--date', type=str, help='Date for function in format YYYY-mm-dd',
                        default=f'{current_date}')
    parser.add_argument('-dr', '--dates_range', type=str, help='Dates for function in format YYYY-mm-dd YYYY-mm-dd',
                        nargs=2)
    parser.add_argument('-a', '--action', help='Choose function, wich you will call',
                        choices=[
                            'week_weather_forecast',
                            'show_weather_forecast',
                            'make_card',
                            'update_database',
                            'extract_data',
                        ])
    args = parser.parse_args()
    presenter = WeatherForecastPresenter(weather_forecast)
    db = DatabaseUpdater(weather_forecast)
    if args.action == 'week_weather_forecast':
        presenter.week_weather_forecast()
    elif args.action == 'show_weather_forecast':
        if args.dates_range is not None:
            call_func_in_dates_range(
                func=presenter.show_weather_forecast, data=weather_forecast,
                start_date=args.dates_range[0], end_date=args.dates_range[1],
            )
        else:
            presenter.show_weather_forecast(args.date)
    elif args.action == 'make_card':
        base = 'python_snippets/external_data/probe.jpg'
        card = WeatherForecastCard(weather_forecast, base)
        if args.dates_range is not None:
            call_func_in_dates_range(
                func=card.run, data=weather_forecast,
                start_date=args.dates_range[0], end_date=args.dates_range[1],
            )
        else:
            card.run(args.date)
    elif args.action == 'update_database':
        if args.dates_range is not None:
            call_func_in_dates_range(
                func=db.update_database, data=weather_forecast,
                start_date=args.dates_range[0], end_date=args.dates_range[1],
            )
        else:
            db.update_database(args.date)
    elif args.action == 'extract_data':
        if args.dates_range is not None:
            call_func_in_dates_range(
                func=db.extract_data, data=weather_forecast,
                start_date=args.dates_range[0], end_date=args.dates_range[1],
            )
        else:
            x, y = db.extract_data(args.date)
            print(x, y)
#зачет!
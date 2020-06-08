# -*- coding: utf-8 -*-

import os, time, shutil, zipfile


# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени создания файла.
# Обработчик файлов делать в обьектном стиле - на классах.
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
# Требования к коду: он должен быть готовым к расширению функциональности. Делать сразу на классах.

class Sorter:

    def __init__(self, zip_file_name, output_folder):
        self.zip_file_name = zip_file_name
        self.output_folder = output_folder

    def sort(self):
        with zipfile.ZipFile(self.zip_file_name) as zfile:
            for file in zfile.namelist():
                date_info = zfile.getinfo(file)
                year = date_info.date_time[0]
                month = date_info.date_time[1]
                new_path = f'{self.output_folder}\\{year}\\{month}'
                if os.path.isdir(new_path):
                    extracts_file = zfile.extract(file, new_path)
                    extract_path = os.path.dirname(extracts_file)
                    shutil.move(extracts_file, new_path)
                    os.removedirs(extract_path)
                else:
                    os.makedirs(new_path)  # Возможно вам пригодится параметр exist_ok=True у этого метода
                    # в этом случае не будут вызываться исключения при попытке создания существующей директории


zip_file_name = 'icons.zip'
output_folder = 'icons_by_year'
sorter = Sorter(zip_file_name, output_folder)
sorter.sort()

# directory = 'icons'
# files = os.walk(directory)
# for d, dirs, files in files:
#     for file in files:
#         path = os.path.join(d, file)
#         file_time_sec = os.path.getctime(path)
#         file_time = time.gmtime(file_time_sec)
#         print(file_time)
#         new_path = f"icons_by_year\\{file_time[0]}\\{file_time[1]}"
#         if os.path.isdir(new_path):
#             shutil.copy2(f"{path}", f"{new_path}")
#         else:
#             os.makedirs(new_path)

# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится ктолько к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
# Для этого пригодится шаблон проектирование "Шаблонный метод" см https://goo.gl/Vz4828
#зачет!
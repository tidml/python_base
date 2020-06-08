# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_data(line):
    if len(line.split(' ')) != 3:
        raise ValueError('Необходим заполнить все поля')
    else:
        name, e_mail, age = line.split(' ')
    if name.isalpha() is False:
        raise NotNameError('Поле имени содержит НЕ только буквы')
    elif '@' not in e_mail or '.' not in e_mail:
        raise NotEmailError('Поле емейл НЕ содержит @ и .(точку)')
    elif int(age) not in range(10, 99):
        raise ValueError('Необходим возраст от 10 до 99 лет')


def check_input_data(input_file, bad_registration, good_registration):
    with open(input_file, 'r', encoding='utf8') as file:
        bad = open(bad_registration, 'a', encoding='utf8')
        good = open(good_registration, 'a', encoding='utf8')
        for line in file:
            line = line[:-1]
            try:
                check_data(line)
            except (ValueError, NotNameError, NotEmailError) as exc:
                bad.write(f'{line} | Ошибка! {exc} \n')
            else:
                good.write(f'{line} \n')
        bad.close()
        good.close()


input_file = 'registrations.txt'
bad_registration = 'bad_registration.txt'
good_registration = 'good_registration.txt'
check_input_data(input_file, bad_registration, good_registration)

#Зачет!
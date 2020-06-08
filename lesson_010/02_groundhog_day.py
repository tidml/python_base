# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.

from random import randint

ENLIGHTENMENT_CARMA_LEVEL = 777


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    dice = randint(1, 13)  # Шанс должен быть 1 из 13
    if dice == 8:
        error_list = [IamGodError('Я бог'), DrunkError('Напился'),
                      CarCrashError('Попал в аварию'), GluttonyError('Объелся'),
                      DepressionError('В депрессии'), SuicideError('Пытался покончить с собой')]
        choosing_error = randint(0, 5)
        raise error_list[choosing_error]
    else:
        return dice


carma = 0
while carma < ENLIGHTENMENT_CARMA_LEVEL:
    with open('log.txt', 'a', encoding='utf8') as file:
        try:
            carma += one_day()
        except IamGodError as exc:
            print(f'Ошибка {exc}. Начал думать, что я бог \n')
            file.write(f'Ошибка {exc}. Начал думать, что я бог \n')
        except DrunkError as exc:
            print(f'Ошибка {exc}. Надо меньше пить')
            file.write(f'Ошибка {exc}. Надо меньше пить \n')
        except CarCrashError as exc:
            print(f'Ошибка {exc}. Нужно водить аккуратнее')
            file.write(f'Ошибка {exc}. Нужно водить аккуратнее \n')
        except GluttonyError as exc:
            print(f'Ошибка {exc}. Нужно перестать бездумно есть')
            file.write(f'Ошибка {exc}. Нужно перестать бездумно есть \n')
        except DepressionError as exc:
            print(f'Ошибка {exc}. Нужно найти какие-то плюсы в жизни')
            file.write(f'Ошибка {exc}. Нужно найти какие-то плюсы в жизни \n')
        except SuicideError as exc:
            print(f'Ошибка {exc}. Нужно ценить жизнь')
            file.write(f'Ошибка {exc}. Нужно ценить жизнь \n')
        else:
            print(f'Текущий уровень кармы: {carma}')
            file.write(f'Текущий уровень кармы: {carma} \n')

# https://goo.gl/JnsDqu
#Зачет!
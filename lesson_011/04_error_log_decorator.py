# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'

def log_errors_in_file(file_name):
    def log_errors(func):
        def surrogate(*args):
            bad = open(file_name, 'a', encoding='utf8')
            try:
                func(*args)
            except Exception as exc:
                bad.write(f'Функция: "{func.__name__}". '
                          f'Параметры: {str(args)[1:-2]}. '
                          f'Ошибка: {str(exc.__class__)[7:-1]}. '
                          f'Сообщение: {exc} \n')
                raise exc
            bad.close()

        return surrogate

    return log_errors


# Проверить работу на следующих функциях
file_name = 'function_errors_perky.log'


@log_errors_in_file(file_name)
def perky(param):
    return param / 0


# perky(42)
# result = log_errors(perky, 42)
# print(result)
# x = log_errors(perky)
# result = x(42)
# print(result)

file_name_2 = 'function_errors_line.log'


@log_errors_in_file(file_name_2)
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')

# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
#зачет!
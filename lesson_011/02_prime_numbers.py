# -*- coding: utf-8 -*-


# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers


print(get_prime_numbers(100))


# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:

    def __init__(self, n):
        self.number = 1
        self.n = n

    def __iter__(self):
        self.number = 1
        return self

    def __next__(self):
        while self.number <= self.n:
            if self.number >= self.n:
                raise StopIteration()
            self.number += 1
            for j in range(2, self.number):
                if self.number % j == 0:
                    break
            else:
                return self.number


prime_number_iterator = PrimeNumbers(n=100)
# for number in prime_number_iterator:
#     print(number)
#
#
# # Часть 2
# # Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# # Распечатать все простые числа до 10000 в столбик
#
#
print(f'/{" Часть 2 ":=^30}\\')

# for number_g, number_i in zip(prime_numbers_generator(n=100), prime_number_iterator):
#     print(number_g == number_i)


# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)


print(f'/{" Часть 3 ":=^30}\\')


def is_this_lucky_number(number):
    number_of_symbols = len(str(number))
    list_of_symbols = list(str(number))
    if number_of_symbols % 2 != 0:
        pop_index = int(number_of_symbols / 2)
        list_of_symbols.pop(pop_index)
        number_of_symbols = len(list_of_symbols)
    first_half_sum = 0
    second_half_sum = 0
    border = int((number_of_symbols / 2))
    for index in range(0, border):
        first_half_sum += int(list_of_symbols[index])
    for index in range(border, number_of_symbols):
        second_half_sum += int(list_of_symbols[index])
    if first_half_sum == second_half_sum:
        print(f'{number} - счастливое число!')
    else:
        print(f'{number} - обычное число!')


def is_this_palindrome_number(number):
    list_of_symbols = list(str(number))
    reverse_list = list_of_symbols[::-1]
    if list_of_symbols == reverse_list:
        print(f'{number} - число палиндром')
    else:
        print(f'{number} - обычное число')


def checking_number(verification_function):
    def decorate_number(func):
        def surrogate(*args):
            result = func(*args)
            for number in result:
                verification_function(number)
                yield

        return surrogate

    return decorate_number


@checking_number(is_this_lucky_number)
def prime_numbers_generator(n):
    for number in range(2, n):
        for j in range(2, number):
            if number % j == 0:
                break
        else:
            yield number


prime_number = prime_numbers_generator(1000)
for number in prime_number:
    if number is not None:
        print(number)
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
#зачет!
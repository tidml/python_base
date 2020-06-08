from random import randint

_random_number = set()
bulls = 0
cows = 0
user_input = str()


def get_random_number():
    global _random_number
    _random_number.clear()
    while len(_random_number) != 4:
        _random_number.add(randint(0, 9))
        if list(_random_number)[0] == 0:
            _random_number.pop()


def verify_input():
    global user_input
    user_input = input('Какое число я загадал?')
    while len(set(user_input)) != 4 or int(user_input) < 1000:
        print('Число не должно начинаться с 0 и его цифры должны быть разные')
        user_input = input('Какое число я загадал?')


def count_bulls_and_cows():
    global bulls, cows, user_input
    bulls = cows = 0
    for i, number in enumerate(user_input):
        user_number = int(number)
        random_number = list(_random_number)
        bulls += 1 if random_number[i] == user_number else 0
        cows += random_number.count(user_number)
    print(f'Быков: {bulls}', f'Коров: {cows}', sep='\n')


def checking_user_number():
    global bulls, cows, user_input
    count_bulls_and_cows()
    if bulls != 4:
        return False
    else:
        return True


if __name__ == "__main__":
    checking_user_number()

import os
from operator import itemgetter


def get_path(wanted_folder):
    folder = os.listdir(wanted_folder)
    for file in folder:
        file_name = f'{wanted_folder}/{file}'
        yield file_name


def sort(diction):
    sorted_volatility_list = sorted(diction.items(), key=itemgetter(1), reverse=False)
    zero_volatility = []
    for paper, number in sorted_volatility_list:
        if number != 0:
            break
        data = (paper, number)
        zero_volatility.append(data)
    for data in zero_volatility:
        sorted_volatility_list.remove(data)
    return sorted_volatility_list, zero_volatility


def output_data(securities_volatility, zero_volatility):
    min_volatility = securities_volatility[0:3]
    max_volatility = securities_volatility[:-4:-1]
    zero_papers = dict(zero_volatility)
    print(f'\n{" Максимальная волатильность ":=^50}')
    for paper, number in max_volatility:
        print(f'{paper:^24} - {number:>14} %')
    print(f'\n{" Мминимальная волатильность ":=^50}')
    for paper, number in min_volatility:
        print(f'{paper:^24} - {number:>14} %')
    print(f'\n{" Нулевая волатильность ":=^50}')
    print(*zero_papers.keys())
# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
#
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
import multiprocessing

from path_sort_data import get_path, sort, output_data


class SecuritiesVolatility(multiprocessing.Process):

    def __init__(self, file_name, collector, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.file_name = file_name
        self.collector = collector
        self.securities = {}

    def volatility_calculation(self):
        with open(self.file_name, 'r', encoding='utf8') as file:
            prices = []
            for line in file:
                if line != 'SECID,TRADETIME,PRICE,QUANTITY\n':
                    elems = line.split(',')
                    price = float(elems[2])
                    security_paper = elems[0]
                    prices.append(price)
            min_price = min(prices)
            max_price = max(prices)
            average_price = (max_price + min_price) / 2
            volatility = round(((max_price - min_price) / average_price) * 100, 2)
            self.securities[security_paper] = volatility
            self.collector.put(self.securities)

    def run(self):
        self.volatility_calculation()


if __name__ == '__main__':

    securities_volatility = {}

    wanted_folder = 'trades'
    path = get_path(wanted_folder)

    collector = multiprocessing.Queue()
    data_securities = [SecuritiesVolatility(file_name=file, collector=collector) for file in path]

    for process in data_securities:
        process.start()

    for process in data_securities:
        process.join()

    while not collector.empty():
        data = collector.get()
        securities_volatility.update(data)

    data = sort(securities_volatility)
    securities_volatility = data[0]
    zero_volatility = data[1]
    output_data(securities_volatility, zero_volatility)
# зачет!

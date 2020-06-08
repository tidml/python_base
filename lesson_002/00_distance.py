#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

distances = {}

moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

moscow_to_london = (((moscow[0] - london[0]) ** 2 + (moscow[1] - london[1]) ** 2) ** 0.5)
moscow_to_paris = (((moscow[0] - paris[0]) ** 2 + (moscow[1] - paris[1]) ** 2) ** 0.5)
london_to_paris = (((london[0] - paris[0]) ** 2 + (london[1] - paris[1]) ** 2) ** 0.5)
london_to_moscow = moscow_to_london

distances['Moscow'] = {}
distances['Moscow']['London'] = moscow_to_london
distances['Moscow']['Paris'] = moscow_to_paris
distances['London'] = {}
distances['London']['Paris'] = london_to_paris
distances['London']['Moscow'] = london_to_moscow
distances['Paris'] = {}
distances['Paris']['Moscow'] = moscow_to_paris
distances['Paris']['London'] = london_to_paris

pprint(distances)

#зачет!
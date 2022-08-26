import csv
import re
from .utils.most_ordered_dish import get_most_ordered_dish_by_customer


def analyze_log(path_to_file):
    if not re.search('csv$', path_to_file):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as file:
            orders_reader = csv.reader(file, delimiter=',', quotechar='"')
            maria_most_ordered_dish = get_most_ordered_dish_by_customer(
                orders_reader,
                'maria'
            )

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

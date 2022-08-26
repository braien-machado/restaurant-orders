import csv
import re
from .utils.most_ordered_dish import (
    get_most_ordered_dish_by_customer,
    get_customer_order_quantity_by_dish
)


def analyze_log(path_to_file):
    if not re.search('csv$', path_to_file):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as file:
            orders_list = list(csv.reader(file, delimiter=',', quotechar='"'))
            maria_most_ordered_dish = get_most_ordered_dish_by_customer(
                orders_list,
                'maria'
            )
            arnaldo_hamburguer_orders = get_customer_order_quantity_by_dish(
                orders_list,
                'arnaldo',
                'hamburguer'
            )
            print(maria_most_ordered_dish)
            print(arnaldo_hamburguer_orders)

    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")

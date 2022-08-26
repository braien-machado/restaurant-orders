from collections import Counter
import csv
import re


def get_orders_by_customer(orders, customer_name):
    return [order for order in orders if order[0] == customer_name]


def most_ordered_dish_by_customer(orders, customer_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    return Counter([order[1] for order in customer_orders]).most_common()[0][0]


def customer_order_quantity_by_dish(orders, customer_name, dish_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    dishes_quantity = Counter([order[1] for order in customer_orders])

    for dish in dishes_quantity:
        if dish_name in dish:
            return dishes_quantity[dish]

    return 0


def never_ordered_dishes_by_customer(orders, customer_name):
    all_dishes = {order[1] for order in orders}
    customer_orders = get_orders_by_customer(orders, customer_name)
    customer_dishes = {order[1] for order in customer_orders}

    return all_dishes.difference(customer_dishes)


def days_customer_never_went(orders, customer_name):
    restaurant_days_opened = {order[2] for order in orders}
    customer_orders = get_orders_by_customer(orders, customer_name)
    client_days = {order[2] for order in customer_orders}

    return restaurant_days_opened.difference(client_days)



def csv_reader(path_to_file):
    if 'csv' not in path_to_file:
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    try:
        with open(path_to_file, encoding='utf-8') as file:
            return list(csv.reader(file, delimiter=',', quotechar='"'))
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")


def analyze_log(path_to_file):
    orders_list = csv_reader(path_to_file)
    maria_most_ordered_dish = most_ordered_dish_by_customer(
        orders_list,
        'maria'
    )
    arnaldo_hamburguer_orders = customer_order_quantity_by_dish(
        orders_list,
        'arnaldo',
        'hamburguer'
    )
    joao_never_ordered_dishes = never_ordered_dishes_by_customer(
        orders_list,
        'joao'
    )
    days_joao_never_appeared = days_customer_never_went(
        orders_list,
        'joao'
    )

    file = open('data/mkt_campaign.txt', mode='w')
    LINES = [
        f'{maria_most_ordered_dish}\n',
        f'{arnaldo_hamburguer_orders}\n',
        f'{joao_never_ordered_dishes}\n',
        f'{days_joao_never_appeared}\n',
    ]
    file.writelines(LINES)

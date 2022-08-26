def get_orders_by_customer(orders, customer_name):
    return [
        order
        for order in orders
        if order[0] == customer_name
    ]


def get_list_values_quantity(orders):
    values_quantity = {}
    for order in orders:
        if order[1] not in values_quantity:
            values_quantity[order[1]] = 1
        else:
            values_quantity[order[1]] += 1

    return values_quantity


def get_key_by_bigger_value(dict: dict):
    key_and_bigger_value = ['', 0]
    for key, value in dict.items():
        if value > key_and_bigger_value[1]:
            key_and_bigger_value = [key, value]

    return key_and_bigger_value


def get_most_ordered_dish_by_customer(orders, customer_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    dishes_quantity = get_list_values_quantity(customer_orders)

    return get_key_by_bigger_value(dishes_quantity)[0]


def get_customer_order_quantity_by_dish(orders, customer_name, dish_name):
    customer_orders = get_orders_by_customer(orders, customer_name)
    dishes_quantity = get_list_values_quantity(customer_orders)

    if dish_name in dishes_quantity:
        return dishes_quantity[dish_name]

    return 0

def get_key_by_bigger_value(dict: dict):
    key_and_bigger_value = ['', 0]
    for key, value in dict.items():
        if value > key_and_bigger_value[1]:
            key_and_bigger_value = [key, value]

    return key_and_bigger_value


def get_most_ordered_dish_by_customer(orders, customer_name):
    dishes_quantity = {}
    for order in orders:
        if order[0] == customer_name and order[1] not in dishes_quantity:
            dishes_quantity[order[1]] = 1
        elif order[0] == customer_name and order[1] in dishes_quantity:
            dishes_quantity[order[1]] += 1

    return get_key_by_bigger_value(dishes_quantity)[0]

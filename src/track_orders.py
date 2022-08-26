from collections import Counter


class TrackOrders:
    def __init__(self):
        self.orders = []
    # aqui deve expor a quantidade de estoque

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append([customer, order, day])

    def get_orders_per_customer(self, customer):
        return [order for order in self.orders if order[0] == customer]

    def get_most_ordered_dish_per_customer(self, customer):
        customer_orders = self \
            .get_orders_per_customer(customer)
        return Counter([order[1] for order in customer_orders]) \
            .most_common()[0][0]

    def get_never_ordered_per_customer(self, customer):
        all_dishes = {order[1] for order in self.orders}
        customer_orders = self.get_orders_per_customer(customer)
        customer_dishes = {order[1] for order in customer_orders}
        return all_dishes.difference(customer_dishes)

    def get_days_never_visited_per_customer(self, customer):
        restaurant_days_opened = {order[2] for order in self.orders}
        customer_orders = self.get_orders_per_customer(customer)
        client_days = {order[2] for order in customer_orders}
        return restaurant_days_opened.difference(client_days)

    def get_busiest_day(self):
        return Counter([order[2] for order in self.orders]).most_common()[0][0]

    def get_least_busy_day(self):
        return Counter([order[2] for order in self.orders]) \
            .most_common()[-1][0]

class InventoryControl:
    INGREDIENTS = {
        'hamburguer': ['pao', 'carne', 'queijo'],
        'pizza': ['massa', 'queijo', 'molho'],
        'misto-quente': ['pao', 'queijo', 'presunto'],
        'coxinha': ['massa', 'frango'],
    }
    MINIMUM_INVENTORY = {
        'pao': 50,
        'carne': 50,
        'queijo': 100,
        'molho': 50,
        'presunto': 50,
        'massa': 50,
        'frango': 50,
    }

    def __init__(self):
        self.storage = dict(**self.MINIMUM_INVENTORY)

    def add_new_order(self, customer, order, day):
        if order not in self.get_available_dishes():
            return False
        ingredients = self.INGREDIENTS[order]
        for ingredient in ingredients:
            self.storage[ingredient] -= 1

    def get_quantities_to_buy(self):
        quantities_to_buy = {}
        for ingredient in self.storage:
            if self.MINIMUM_INVENTORY[ingredient] > self.storage[ingredient]:
                quantities_to_buy.update(
                    {
                        ingredient: self
                        .MINIMUM_INVENTORY[ingredient] - self
                        .storage[ingredient]
                    }
                )
            else:
                quantities_to_buy.update({ingredient: 0})
        return quantities_to_buy

    def get_available_dishes(self):
        available_ingredients = {
            ingredient
            for ingredient in self.storage
            if self.storage[ingredient] > 0
        }
        available_dishes = set()
        for dish in self.INGREDIENTS:
            ingredients = {ingredient for ingredient in self.INGREDIENTS[dish]}
            if ingredients.issubset(available_ingredients):
                available_dishes.add(dish)

        return available_dishes

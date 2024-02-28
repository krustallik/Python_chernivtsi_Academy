class ShopOrder:
    def __init__(self, name=None, price=0.0, count_of_ordered_items=0):
        self.name = name
        self.price = price
        self.count_of_ordered_items = count_of_ordered_items

    def set_states(self, name, price, count_of_ordered_items):
        self.name = name
        self.price = price
        self.count_of_ordered_items = count_of_ordered_items

    def get_price(self):
        return self.price * self.count_of_ordered_items

    def print_order(self):
        print(f"Товар: {self.name}, Ціна за одиницю: {self.price}₴, Кількість: {self.count_of_ordered_items}, Загальна ціна: {self.get_price()}₴")

# Створення об'єкта із використанням конструктора
order1 = ShopOrder("Milk", 10, 15)
order1.print_order()

# Створення об'єкта та встановлення стану за допомогою метода
order2 = ShopOrder()
order2.set_states("Bread", 7, 25)
order2.print_order()

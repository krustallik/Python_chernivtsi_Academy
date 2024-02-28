
#в першім способі інформацію надаємо при створенні в другому за допомогою метода
class ShopOrder1:
    def __init__(self, name=None, price=0.0, count_of_ordered_items=0):
        self.name = name
        self.price = price
        self.count_of_ordered_items = count_of_ordered_items
    def get_price(self):
        return self.price * self.count_of_ordered_items

milk = ShopOrder1("Milk",10,15)
print("Загальна ціна товару: ",milk.get_price())


class ShopOrder2:
    def get_price(self):
        return self.price * self.count_of_ordered_items
    def set_states(self,name=None, price=0.0, count_of_ordered_items=0):
        self.name = name
        self.price = price
        self.count_of_ordered_items = count_of_ordered_items


item = ShopOrder2()
item.set_states("bread",7,25)
print("Загальна ціна товару: ",item.get_price())


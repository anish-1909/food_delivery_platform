# import menu from member1
from member1 import menu_catalog

class Item:
    def __init__(self, name):
        self.name = name
        self.price = menu_catalog[name]

    def __str__(self):
        return f"{self.name} - {self.price}"

class Order:
    count = 1   

    def __init__(self, customer, items_list, restaurant):
        self.customer = customer
        self.restaurant = restaurant

        self.items = [Item(i) for i in items_list]

        self.__order_id = Order.count
        Order.count += 1

        self._status = "Pending"

    # total price
    def total(self):
        return sum(i.price for i in self.items)

    # number of items
    def __len__(self):
        return len(self.items)

    # receipt
    def receipt(self):
        print("Customer:", self.customer)
        for i in self.items:
            print(i)
        print("Total:", self.total())

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, val):
        if val in ["Pending", "Delivered"]:
            self._status = val
        else:
            print("Invalid status")

# inheritance
class PremiumOrder(Order):
    def total(self):
        return super().total() * 0.9

o = Order("alice", ["pizza","burger","salad"], "Spice Hub")

print("len(o) →", len(o))
print("o.total() →", o.total())

po = PremiumOrder("bob", ["sushi","pasta"], "Zen Kitchen")
print("po.total() →", po.total())

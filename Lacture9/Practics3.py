class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self,odr2):
        return self.price > Ord2.price

Ord1 = Order("Chips",20)
Ord2 = Order("Tea",15)

print(Ord1 > Ord2)
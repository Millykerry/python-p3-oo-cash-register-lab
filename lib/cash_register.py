class CashRegister:
    def __init__(self, discount=0):
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction = 0

    def add_item(self, name, price, quantity=1):
        self.total += price * quantity
        for _ in range(quantity):
            self.items.append(name)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total *= (1 - self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        self.total -= self.last_transaction
        self.last_transaction = 0


class Order:
    def __init__(self, menu):
        self.menu = menu
        self.items = {}
        self.discount_name = "No Discount"
        self.discount_rate = 0.0

    def add_item(self, code, quantity):
        if code in self.items:
            self.items[code] += quantity
        else:
            self.items[code] = quantity

    def calculate_subtotal(self):
        subtotal = 0

        for code, quantity in self.items.items():
            subtotal += self.menu.get_price(code) * quantity

        return subtotal

    def apply_discount(self, name, rate):
        self.discount_name = name
        self.discount_rate = rate

    def get_discount_amount(self):
        return self.calculate_subtotal() * self.discount_rate

    def calculate_total(self):
        return self.calculate_subtotal() - self.get_discount_amount()
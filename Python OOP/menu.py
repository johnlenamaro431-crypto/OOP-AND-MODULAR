class Menu:
    def __init__(self):
        self.items = {
            "B1": {"name": "Classic Burger", "price": 85.00},
            "B2": {"name": "Cheese Burger", "price": 99.00},
            "B3": {"name": "Chicken Burger", "price": 95.00},
            "C1": {"name": "1-pc Fried Chicken", "price": 89.00},
            "C2": {"name": "2-pc Fried Chicken", "price": 149.00},
            "R1": {"name": "Chicken with Rice", "price": 109.00},
            "S1": {"name": "Regular Fries", "price": 49.00},
            "S2": {"name": "Large Fries", "price": 69.00},
            "D1": {"name": "Soft Drink", "price": 39.00},
            "D2": {"name": "Iced Tea", "price": 45.00},
            "D3": {"name": "Bottled Water", "price": 30.00},
            "DS": {"name": "Chocolate Sundae", "price": 55.00}
        }

    def has_item(self, code):
        return code in self.items

    def get_name(self, code):
        return self.items[code]["name"]

    def get_price(self, code):
        return self.items[code]["price"]

    def display(self):
        print("\n" + "=" * 55)
        print("             BYTE & BITE FAST FOOD")
        print("           Delicious Food, Fast Service!")
        print("=" * 55)

        print(f"{'CODE':<8}{'MENU ITEM':<30}{'PRICE':>15}")
        print("-" * 55)

        for code, item in self.items.items():
            print(f"{code:<8}{item['name']:<30}₱{item['price']:>12.2f}")

        print("-" * 55)
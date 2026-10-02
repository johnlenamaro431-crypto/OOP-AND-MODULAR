class Receipt:
    def __init__(self, order, payment):
        self.order = order
        self.payment = payment

    def get_change(self):
        return self.payment - self.order.calculate_total()

    def print_receipt(self):
        order = self.order
        subtotal = order.calculate_subtotal()
        discount_amount = order.get_discount_amount()
        total = order.calculate_total()

        print("\n\n")
        print("=" * 60)
        print("                    BYTE & BITE")
        print("                  FAST FOOD HOUSE")
        print("            Thank you for ordering!")
        print("=" * 60)

        print(f"{'ITEM':<25}{'QTY':>5}{'PRICE':>12}{'TOTAL':>15}")
        print("-" * 60)

        for code, quantity in order.items.items():
            item_name = order.menu.get_name(code)
            item_price = order.menu.get_price(code)
            item_total = item_price * quantity

            print(
                f"{item_name:<25}"
                f"{quantity:>5}"
                f"₱{item_price:>10.2f}"
                f"₱{item_total:>13.2f}"
            )

        print("-" * 60)
        print(f"{'SUBTOTAL:':<43}₱{subtotal:>15.2f}")
        print(f"{order.discount_name + ':':<43}-₱{discount_amount:>14.2f}")
        print(f"{'TOTAL:':<43}₱{total:>15.2f}")
        print("-" * 60)
        print(f"{'CASH:':<43}₱{self.payment:>15.2f}")
        print(f"{'CHANGE:':<43}₱{self.get_change():>15.2f}")
        print("=" * 60)

        print("              THIS SERVES AS YOUR RECEIPT")
        print("                PLEASE COME AGAIN!")
        print("=" * 60)
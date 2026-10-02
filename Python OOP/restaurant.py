from menu import Menu
from order import Order
from receipt import Receipt


class Restaurant:
    def __init__(self):
        self.menu = Menu()

    def get_yes_no(self, message):
        while True:
            answer = input(message).strip().upper()

            if answer == "Y":
                return True
            elif answer == "N":
                return False
            else:
                print("Invalid input. Please enter Y or N only.")

    def get_menu_item(self):
        while True:
            code = input("\nEnter menu code: ").strip().upper()

            if self.menu.has_item(code):
                return code
            else:
                print("Invalid menu code. Please choose an item from the menu.")

    def get_quantity(self):
        while True:
            try:
                quantity = int(input("Enter quantity : "))

                if quantity > 0:
                    return quantity
                else:
                    print("Quantity must be greater than 0.")

            except ValueError:
                print("Invalid quantity. Please enter a whole number.")

    def get_discount(self, order):
        print("\n" + "-" * 55)
        print("AVAILABLE DISCOUNTS")
        print("-" * 55)
        print("1. No Discount")
        print("2. Student Discount - 5%")
        print("3. Senior Citizen / PWD Discount - 20%")
        print("-" * 55)

        while True:
            choice = input("Select discount [1-3]: ").strip()

            if choice == "1":
                order.apply_discount("No Discount", 0.0)
                return
            elif choice == "2":
                order.apply_discount("Student Discount (5%)", 0.05)
                return
            elif choice == "3":
                order.apply_discount("Senior/PWD Discount (20%)", 0.20)
                return
            else:
                print("Invalid choice. Please select 1, 2, or 3.")

    def get_payment(self, total):
        while True:
            try:
                payment = float(input(f"\nAmount to pay: ₱{total:.2f}\nEnter cash     : ₱"))

                if payment >= total:
                    return payment
                else:
                    shortage = total - payment
                    print(f"Insufficient payment. You still need ₱{shortage:.2f}.")

            except ValueError:
                print("Invalid amount. Please enter a valid number.")

    def run(self):
        order = Order(self.menu)

        self.menu.display()

        if not self.get_yes_no("\nWould you like to order? [Y/N]: "):
            print("\nThank you for visiting Byte & Bite!")
            print("We hope to serve you next time.\n")
            return

        while True:
            code = self.get_menu_item()
            quantity = self.get_quantity()

            order.add_item(code, quantity)

            item_name = self.menu.get_name(code)
            item_total = self.menu.get_price(code) * quantity

            print("\nItem successfully added!")
            print(f"{quantity} x {item_name} = ₱{item_total:.2f}")

            if not self.get_yes_no("\nWould you like to order another item? [Y/N]: "):
                break

            self.menu.display()

        self.get_discount(order)

        payment = self.get_payment(order.calculate_total())

        receipt = Receipt(order, payment)
        receipt.print_receipt()
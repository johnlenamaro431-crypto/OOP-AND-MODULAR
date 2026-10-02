from menu import menu


def get_yes_no(message):
    while True:
        answer = input(message).strip().upper()

        if answer == "Y":
            return True
        elif answer == "N":
            return False
        else:
            print("Invalid input. Please enter Y or N only.")


def get_menu_item():
    while True:
        item_code = input("\nEnter menu code: ").strip().upper()

        if item_code in menu:
            return item_code
        else:
            print("Invalid menu code. Please choose an item from the menu.")


def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity : "))

            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than 0.")

        except ValueError:
            print("Invalid quantity. Please enter a whole number.")


def get_payment(total):
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
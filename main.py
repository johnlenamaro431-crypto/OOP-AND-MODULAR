from menu import menu
from display import print_menu, print_receipt
from validation import get_yes_no, get_menu_item, get_quantity, get_payment
from order import add_order, calculate_subtotal
from discount import get_discount


def main():
    orders = {}

    print_menu()

    wants_to_order = get_yes_no("\nWould you like to order? [Y/N]: ")

    if not wants_to_order:
        print("\nThank you for visiting Byte & Bite!")
        print("We hope to serve you next time.\n")
        return

    while True:
        item_code = get_menu_item()
        quantity = get_quantity()

        add_order(orders, item_code, quantity)

        item_name = menu[item_code]["name"]
        item_total = menu[item_code]["price"] * quantity

        print("\nItem successfully added!")
        print(f"{quantity} x {item_name} = ₱{item_total:.2f}")

        order_again = get_yes_no("\nWould you like to order another item? [Y/N]: ")

        if not order_again:
            break

        print_menu()

    subtotal = calculate_subtotal(orders)

    discount_name, discount_amount = get_discount(subtotal)

    total = subtotal - discount_amount

    payment = get_payment(total)

    print_receipt(orders, subtotal, discount_name,
                  discount_amount, total, payment)


main()
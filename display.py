from menu import menu


def print_header():
    print("\n" + "=" * 55)
    print("             BYTE & BITE FAST FOOD")
    print("           Delicious Food, Fast Service!")
    print("=" * 55)


def print_menu():
    print_header()

    print(f"{'CODE':<8}{'MENU ITEM':<30}{'PRICE':>15}")
    print("-" * 55)

    for code, item in menu.items():
        print(f"{code:<8}{item['name']:<30}₱{item['price']:>12.2f}")

    print("-" * 55)


def print_receipt(orders, subtotal, discount_name,
                  discount_amount, total, payment):
    change = payment - total

    print("\n\n")
    print("=" * 60)
    print("                    BYTE & BITE")
    print("                  FAST FOOD HOUSE")
    print("            Thank you for ordering!")
    print("=" * 60)

    print(f"{'ITEM':<25}{'QTY':>5}{'PRICE':>12}{'TOTAL':>15}")
    print("-" * 60)

    for item_code, quantity in orders.items():
        item_name = menu[item_code]["name"]
        item_price = menu[item_code]["price"]
        item_total = item_price * quantity

        print(
            f"{item_name:<25}"
            f"{quantity:>5}"
            f"₱{item_price:>10.2f}"
            f"₱{item_total:>13.2f}"
        )

    print("-" * 60)
    print(f"{'SUBTOTAL:':<43}₱{subtotal:>15.2f}")
    print(f"{discount_name + ':':<43}-₱{discount_amount:>14.2f}")
    print(f"{'TOTAL:':<43}₱{total:>15.2f}")
    print("-" * 60)
    print(f"{'CASH:':<43}₱{payment:>15.2f}")
    print(f"{'CHANGE:':<43}₱{change:>15.2f}")
    print("=" * 60)

    print("              THIS SERVES AS YOUR RECEIPT")
    print("                PLEASE COME AGAIN!")
    print("=" * 60)
from menu import menu


def add_order(orders, item_code, quantity):
    if item_code in orders:
        orders[item_code] += quantity
    else:
        orders[item_code] = quantity


def calculate_subtotal(orders):
    subtotal = 0

    for item_code, quantity in orders.items():
        subtotal += menu[item_code]["price"] * quantity

    return subtotal
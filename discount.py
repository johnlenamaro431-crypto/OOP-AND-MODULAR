def get_discount(subtotal):
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
            return "No Discount", 0
        elif choice == "2":
            return "Student Discount (5%)", subtotal * 0.05
        elif choice == "3":
            return "Senior/PWD Discount (20%)", subtotal * 0.20
        else:
            print("Invalid choice. Please select 1, 2, or 3.")
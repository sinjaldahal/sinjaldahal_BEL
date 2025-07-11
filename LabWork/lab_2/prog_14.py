'''
**Build a dictionary where the keys are product names and the values are their prices. 
Implement options to:**

a. Add a new product
b. Update price of an existing product
c. Find products within a given price range

'''


products = {
    "pen": 10,
    "notebook": 50,
    "eraser": 5,
    "pencil": 7
}


def add_product():
    name = input("Enter product name: ").lower()
    if name in products:
        print("Product already exists.")
    else:
        price = float(input("Enter product price: "))
        products[name] = price
        print(f"{name} added with price {price}.")


def update_price():
    name = input("Enter product name to update: ").lower()
    if name in products:
        new_price = float(input(f"Enter new price for {name}: "))
        products[name] = new_price
        print(f"Updated price of {name} to {new_price}.")
    else:
        print("Product not found.")


def find_in_range():
    low = float(input("Enter minimum price: "))
    high = float(input("Enter maximum price: "))
    found = False
    print("Products in range:")
    for name, price in products.items():
        if low <= price <= high:
            print(f"{name}: {price}")
            found = True
    if not found:
        print("No products found in this range.")


while True:
    print("\n--- Product Management Menu ---")
    print("1. Add product")
    print("2. Update price")
    print("3. Find products in price range")
    print("4. Show all products")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        add_product()
    elif choice == '2':
        update_price()
    elif choice == '3':
        find_in_range()
    elif choice == '4':
        print("All Products:")
        for k, v in products.items():
            print(f"{k}: {v}")
    elif choice == '5':
        print("Exiting.")
        break
    else:
        print("Invalid choice.")

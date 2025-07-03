'''
Write a menu-driven program to perform arithmetic operations (+, -, *, /)
based on user choice using conditional statements.

'''


def menu():
    print("Select operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

while True:
    menu()
    choice = input("Enter choice (1/2/3/4) or 'q' to quit: ")
    if choice.lower() == 'q':
        print("Exiting program.")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid input. Please try again.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid number. Please try again.")
        continue

    if choice == '1':
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        if num2 == 0:
            print("Error: Division by zero.")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def calculator():
    while True:
        print("\nSelect operation:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Power (^)")
        print("6. Modulus (%)")
        print("0. Exit")

        choice = input("Enter choice (1/2/3/4/5/6/0): ")

        if choice == "0":
            print("Exiting Calculator. Goodbye!")
            break

        if choice in ["1", "2", "3", "4", "5", "6"]:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == "1":
                    print(f"Result: {num1} + {num2} = {add(num1, num2)}")
                elif choice == "2":
                    print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
                elif choice == "3":
                    print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
                elif choice == "4":
                    print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")
                elif choice == "5":
                    print(f"Result: {num1} ^ {num2} = {power(num1, num2)}")
                elif choice == "6":
                    print(f"Result: {num1} % {num2} = {modulus(num1, num2)}")
            except ValueError:
                print("Invalid input! Please enter numbers only.")
        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    calculator()

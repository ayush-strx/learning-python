def add(num_1, num_2):
    return num_1 + num_2

def subtract(num_1, num_2):
    return num_1 - num_2

def multiply(num_1, num_2):
    return num_1 * num_2

def divide(num_1, num_2):
    if num_2 == 0:
        return "Division by zero is not allowed."
    return num_1 / num_2

def percentage(num_1, num_2):
    return (num_1 * num_2) / 100

def main():
    print("<<---------- Simple Calculator ---------->>")

    while True:
        try:
            operand_1 = float(input("Enter the first number: "))
            operand_2 = float(input("Enter the second number: "))

            print("\n========== Choose operations: ==========")
            print(" +  Addition")
            print(" -  Subtraction")
            print(" *  Multiplication")
            print(" /  Division")
            print(" %  Percentage")
            print("==========================================")

            operation = input("\nEnter your choice: ")

            if operation == "+":
                print(f"Result: {operand_1} + {operand_2} = {add(operand_1, operand_2)}")

            elif operation == "-":
                print(f"Result: {operand_1} - {operand_2} = {subtract(operand_1, operand_2)}")

            elif operation == "*":
                print(f"Result: {operand_1} * {operand_2} = {multiply(operand_1, operand_2)}")

            elif operation == "/":
                print(f"Result: {operand_1} / {operand_2} = {divide(operand_1, operand_2)}")

            elif operation == "%":
                print(f"Result: {operand_2}% of {operand_1} = {percentage(operand_1, operand_2)}")

            else:
                print("Please enter a valid operation.")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

        while True:
            choice = input("\nDo you want to continue (y/n): ").lower()     
            if choice == "y":
                break

            elif choice == "n":
                print("Thank you for using the calculator!")
                return

            else:
                print("Please enter only 'y' or 'n'.")

main()
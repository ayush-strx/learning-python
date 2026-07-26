# Create a program to take two numbers from the user, divide them, and access an element from a fruit list using a user-provided index. Handle ZeroDivisionError if division by zero occurs and handle IndexError if the list index does not exist

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1 / num2
    print("Result:", result)

    fruits = ["Apple", "Mango", "Banana"]
    index = int(input("Enter index: "))

    print("Fruit:", fruits[index])

except ZeroDivisionError:
    print("Cannot divide by zero")

except IndexError:
    print("Index does not exist")
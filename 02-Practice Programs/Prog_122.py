# Create a program to take two numbers from the user, divide them, handle division by zero error using except, and print the result using else when the operation is successful.
try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1/num2
except:
    print("Cannot divide by zero")
else:
    print("Result:",result)
    






# Create a program to divide two numbers entered by the user and handle the error when the second number is zero.

try:
    num1 = int(input("Enter the first number:"))
    num2 = int(input("Enter the second number:"))
    div = num1/num2
    print(div)
except:
    print("You can't divide with zero")
    
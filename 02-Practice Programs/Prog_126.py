# Create a program to divide two numbers entered by the user, handle division by zero using except, and use finally to print "Program execution completed" whether an error occurs or not.

try:
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    result = num1/num2
    print(result)
except:
    print("Cannot divide by zero")
finally:
    print("Program execution completed")
    
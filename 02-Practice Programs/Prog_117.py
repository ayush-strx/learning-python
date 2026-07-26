# Create a program that takes a number from the user and handles the error if the user enters a non-numeric value.

try:
    num = int(input("Enter the number:"))
    print(num)
except:
    print("Invalid Input:")
# Create a program that takes user age as input and handles the error if the user enters an invalid value instead of a number.

try:
    age = int(input("Enter your age:"))
    print(age)
except:
    print("Enter in numbers not a characters")

    
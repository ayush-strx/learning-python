# Create a program to take the user's age as input. If the age is less than 18 or negative, raise a ValueError with a custom message. Otherwise, print "You are eligible" using try-except to handle the exception.

try:
    age = int(input("Enter your age:"))

    if age < 18 or age < 0:
        raise ValueError("You are not eligible")

    print("You are eligible")

except ValueError as e:
    print(e)
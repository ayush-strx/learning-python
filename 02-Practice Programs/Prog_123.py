# Create a program to take the user's age as input, handle invalid input using except, and print a success message using else when the age is entered correctly.

try :
    age = int(input("Enter your age:"))
except: 
    print("Don't enter characters:")
else:
    print("Age is entered succesfully")
# Create a program to take a decimal number from the user and display:
# the value rounded up using ceil()
# the value rounded down using floor()

import math

num = float(input("Enter the decimal number:"))
print("value rounded up:", math.ceil(num))
print("value rounded down:", math.floor(num))
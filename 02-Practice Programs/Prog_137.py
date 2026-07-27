""" Create a program that:
Prints the current date and time.
Prints today's date.
Displays the current date in DD/MM/YYYY format."""

import datetime

print(datetime.datetime.now())

print(datetime.date.today())

today = datetime.date.today()
print(today.strftime("%d/%m/%Y"))
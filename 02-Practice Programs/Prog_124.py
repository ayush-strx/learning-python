# Create a program to open a file named "student.txt", handle FileNotFoundError using except, and print a success message using else when the file opens successfully.
try:
    with open("student.txt","r") as f:
        data = f.read()
except:
    print("File doesn't exist")
else:
    print("Program works succesfully")

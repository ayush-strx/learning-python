# Create a program to access an element from a list using user-provided index, handle invalid index using except, and print the element using else.

try:
    fruits = ["Mango","Banana", "Apple"]
    index = int(input("Enter the index no:"))
    element = fruits(index)
except:
    print("Index out of  range .")
else:
    print("Element is:", fruits[element])




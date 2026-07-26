# Create a file named "count.txt" containing some text. Open the file and print the complete content.

with open("count.txt", "w") as f:
    f.write("Python is a programming language.")

with open("count.txt", "r") as f:
    data = f.read()
    print(data)
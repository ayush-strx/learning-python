# Write five lines into a file using writelines() and then read the complete file using read().

with open("hello.txt", "w") as f:
    data = ["Hi\n", "I\n", "Am\n", "Ayush\n", "Tiwari\n"]
    f.writelines(data)

with open("hello.txt", "r") as f:
    content = f.read()
    print(content)
    
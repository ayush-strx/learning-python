# Read the file "student.txt" line by line using readline() and print the content.

f = open("student.txt","r")
data = f.readline()
print(data)
f.close()
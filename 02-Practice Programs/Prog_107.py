# Read all lines from the file "student.txt" using readlines() and print the list.

f = open("student.txt","r")
data = f.readlines()
print(data)
f.close()
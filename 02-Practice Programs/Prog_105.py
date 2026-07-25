# Create a file named "student.txt" and write your Name, Age, and Course into the file using write().

f = open("student.txt","w")
data = f.write("Ayush\n18\nBsc.CS")
print(data)
f.close()
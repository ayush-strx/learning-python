# Create a file named "hello.txt" and write "Hello Python" into the file using write().

f = open("hello.txt","w")
data = f.write("Hello Python")
print(data)
f.close()
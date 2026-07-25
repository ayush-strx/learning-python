# Open the file "hello.txt" in read mode and print the complete content using read().

f = open("hello.txt","r")
data = f.read()
print(data)
f.close()
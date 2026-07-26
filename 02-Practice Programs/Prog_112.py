# Read a file and print the first line and second line using readline().

f = open("hi.txt","r")
line1 = f.readline()
line2 = f.readline()
print(line1)
print(line2)
f.close()
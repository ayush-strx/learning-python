# Create a file named "notes.txt". Take a note from the user using input() and save it into the file using write().
n = input("Enter your note:")
f = open("notes.txt","w")
data = f.write(n)
f.close()

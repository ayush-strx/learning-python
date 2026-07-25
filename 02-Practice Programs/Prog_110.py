# Create a file named "diary.txt". Add a new diary entry using append mode ("a") without deleting previous entries.

n = input("Enter your data:")
f = open("diary.txt","a")
data = f.write(n)
f.close()

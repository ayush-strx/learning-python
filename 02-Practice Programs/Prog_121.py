# Create a program to open a file named "data.txt" and handle the error if the file does not exist.
try:
    with open("data.txt","r") as f:
        data = f.read()
        print(data)
except:
    print("File doesn't exist.")    
      

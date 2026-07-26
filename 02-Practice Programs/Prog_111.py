# Create a file named "marks.txt" and store marks of three subjects in the file.

f  = open("marks.txt","w")
data = ["Science: 72","\nMath: 60","\nEnglish: 80"]
f.writelines(data)
f.close()
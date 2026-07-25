# Create a file named "languages.txt" and write multiple programming languages (Python, C++, Java, SQL) using writelines().

f = open("languages.txt", "w")
languages= ["Python\n","C++\n","Java\n","SQL\n"]
f.writelines(languages)
f.close()
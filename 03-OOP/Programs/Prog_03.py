
class student:
    college_name = "XYZ"    # Class Attribute  ( Shared by all students)

    def __init__(self, name , course):   #__Init__ Constructor - Automatically called

        self.name = name        # Instance attribute (Unique to each students)
        self.course = course    # Instance attibute

    def hello(self):        # Methods : Function inside a class is called Methods.
        print("Hi",self.name)


s1 = student("Ayush","Bsc.CS")    # Object Creation
s2 = student("Ankit","Bsc.CS")    # Object Creation

print(s1)   # Memory address of Object 1
print(s1.name)
print(s1.course)
print(s1.college_name)
s1.hello()

print(s2)   #Memory address of object 2
print(s2.name)
print(s2.course)
print(s2.college_name)
s2.hello()
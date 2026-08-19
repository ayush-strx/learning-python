# Crate a class student that takes 3 marks and has a method average.

class student:
    def __init__(self,name ,sub1,sub2,sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def average(self):
        print((self.sub1 + self.sub2+self.sub3)/3)

student1 = student("name",70,90,82)

student1.average()

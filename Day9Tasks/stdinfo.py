#Student information system
class Student:
    def __init__(self,name,roll,marks):
        self.name=name
        self.roll=roll
        self.marks=marks
    def display(self):
        print("Name:",self.name)
        print("Roll:",self.roll)
        print("Marks:",self.marks)

s1=Student("Ram",1,85)
s2=Student("Rama",2,85)
s3=Student("Ravi",3,85)
s1.display()
s2.display()
s3.display()

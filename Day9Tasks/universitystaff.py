#University syaff management-Hirarchichal Inheritance
class Staff:
    def __init__(self,name,id):
        self.name=name
        self.id=id
class Proffessor(Staff):
    def display(self):
        print("Proffessor:",self.name,self.id)
class LabAssistant(Staff):
    def display(self):
        print("LabAssistance:",self.name,self.id)
class Administrator(Staff):
    def display(self):
        print("Administrator:",self.name,self.id)
p=Proffessor("Ram",1)
l=LabAssistant("Sita",2)
a=Administrator("Ravi",3)
p.display()
l.display()
a.display()
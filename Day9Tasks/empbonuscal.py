#Employee Bonus calculator-decorators and oops
def bonus(func):
    def wrapper(self):
        self.salary+=1000 #add bonus
        func(self)
    return  wrapper
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    @bonus
    def display(self):
        print(self.name,self.salary)
e=Employee("Ram",5000)
e.display()
    
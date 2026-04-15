#oops 
class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
#dict
employees={}
n=int(input("Enter number of employees:"))
for i in range(n):
    name=input("Enter Name:")
    try:
        salary=float(input("Enter salary:"))
        emp=Employee(name,salary)
        employees[name]=emp
    except:
        print("Invalid salary!")
#save to file
with open("employees.txt","w") as f:
    for emp in employees.values():
        f.write(f"{emp.name}-{emp.salary}\n")
#display employees (access dict)
for emp in employees.values():
    print(emp.name,emp.salary)
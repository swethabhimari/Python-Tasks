#Write initial data into file
with open("employee.txt","w") as f:
    f.write("Ramesh 25000\nSita 30000\nArun 28000")
#Read and disply employee data+find highest salary
max_salary=0
max_employee=""
print("Employee Details:\n")
with open("employee.txt","r") as f:
    for line in f:
        name,salary=line.split()
        salary=int(salary)
        print(name,salary)
        if salary>max_salary:
            max_salary=salary
            max_employee=name
print("\nHighest Salary:",max_employee,max_salary)
#Append new employee
name=input("\nEnter new employee name:")
salary=input("Enter salary:")
with open("employee.txt","a") as f:
    f.write(name+" " +salary+"\n")
print("New employee added!")
    
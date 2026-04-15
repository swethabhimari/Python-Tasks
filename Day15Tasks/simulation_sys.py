import numpy as np
import pandas as pd
import random
import math
#student class
class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
#assign grade
    def grade(self):
        if self.marks>75:
            return "A"
        elif self.marks>50:
            return "B"
        else:
            return "C"
students=[] #list to store std obj
names=["Ravi","Sita","Anil","John"]
try:
    #generate random marks and create objs
    for name in names:
        marks = random.randint(30,100)
        students.append(Student(name,marks))#add to list
    
    #dict to store data 
    data={
        "Name":[],
        "Marks":[],
        "Grade":[]
    }
    #fill dict using loop
    for s in students:
        data["Name"].append(s.name)
        data["Marks"].append(s.marks)
        data["Grade"].append(s.grade())
    df = pd.DataFrame(data) #convert to df
    print(df)
    #calculate avg using math
    if len(data["Marks"]) > 0:
        avg = math.floor(sum(data["Marks"])/len(data["Marks"]))
        # print(df)  #display table
        print("Average:", avg)
    else:
        print("No data available")#display avg
    #save to afile
    df.to_csv("report.csv",index=False)
except Exception as e:
    print("Error:",e)   #handle errors

        
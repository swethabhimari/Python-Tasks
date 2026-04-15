# import numpy as np
# import pandas as pd
import math
print("started")
students=[("Ravi",60),
          ("Ramu",70),
          ("Anil",45),
          ("John",75),
          ("sita",35)]
#convert to dictionary
std_dict=dict(students)
print("data:",std_dict)
#loop to find above 50
above_50=[]
total=0
for name,marks in std_dict.items():
    print("check:",name,marks)
    total+=marks
    if marks>50:
        
        above_50.append(name)
        print("above 50",name,marks)
    else:
        print("below 50",name,marks)
#calculate average
avg=total/len(std_dict)
print("Average:",avg)
#store in a file
with open("students.txt","w") as f:
    f.write(f"Students above 50 marks:{above_50}\n")
    f.write(f"Average Marks:{avg}")


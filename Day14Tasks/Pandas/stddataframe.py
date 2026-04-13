import numpy as np
import pandas as pd
data=pd.DataFrame({
    "Name":["A","B","C"],
    "Math":[80,70,60],
    "Science":[90,60,70]
})
#Add total column
data["Total"]=data["Math"]+data["Science"]
print(data)
#find student with highest total
top_student=data.loc[data["Total"].idxmax()]
print("\nTop Stdent:")
print(top_student)
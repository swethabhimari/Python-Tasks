import numpy as np
import pandas as pd
arr=np.array([[80,90],
             [70,60],
             [85,95]])
df=pd.DataFrame(arr, columns=["Math","Science"])
#add a new coloumn
df["Total"]=df["Math"]+df["Science"]
print(df)
#Find std with highest total
top_student=df["Total"].idxmax()
print("Top Srtudent index:",top_student)
print("Highest total:",df.loc[top_student,"Total"])
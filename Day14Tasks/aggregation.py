import numpy as np
import pandas as pd
arr=np.array([[100,200],
             [150,250],
             [80,120],
             [300,400]])
df=pd.DataFrame(arr,columns=["Sales","Profit"])
#filter rows
filtered=df[df["Sales"]>100]
#avg profit
avg_profit=filtered["Profit"].mean()
print(filtered)
print("Average Profit:",avg_profit)
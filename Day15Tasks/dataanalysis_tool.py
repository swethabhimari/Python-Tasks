import numpy as np
import pandas as pd
#generate marks
marks = np.random.randint(30,100,5)
#convert to dataframe
df = pd.DataFrame({"Marks":marks})
#conditions to filter passing students
passing=df[df["Marks"]>50]
#mean total
mean_marks=np.mean(marks)
#loop to print
print("All Marks:")
for m in marks:
    print(m)
print("\npassing Students:")
print(passing)
print("\nMean:",mean_marks)

import pandas as pd
df=pd.DataFrame({
    "Name":["A","B","C","D"],
    "Marks":[50,80,30,90]
    })
#create status column
df["Status"]=df["Marks"].apply(lambda x:"PASS" if x>=50 else "FAIL")
print(df)
#filter passed students
passed=df[df["Status"]=="PASS"]
print("\nPassed Students:")
print(passed)
#avg marks
avg=passed["Marks"].mean()
print("\n Avg marks of passed students is:",avg)
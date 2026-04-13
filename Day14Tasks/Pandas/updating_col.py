import pandas as pd
df=pd.DataFrame({
    "Price":[100,200,300]
    })
#add discount (10)%
df["Discount"]=df["Price"]*0.10
#add final price
df["Final Price"]=df["Price"]-df["Discount"]
print(df)

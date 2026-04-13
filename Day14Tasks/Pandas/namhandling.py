import numpy as np
import pandas as pd
cities={"Delhi":2000000,"Mumbai":3000000,"Chennai":1500000}
#create series with required index
S=pd.Series(cities,index=["Delhi","Chennai","Banglore"])
print(S)
#find missing values
missing=S[S.isna()]
print("Missing cities:")
print(missing)
import numpy as np
import pandas as pd
S=pd.Series([100,200,300,400],index=["A","B","C","D"])
#Access A nd B
subset=S[["B","D"]]
print(subset)
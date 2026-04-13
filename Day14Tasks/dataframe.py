import numpy as np
import pandas as pd
data=np.array([[1,2],[3,4],[6,6]])
col_names=pd.DataFrame(data,columns=["X","Y"])
print(col_names)
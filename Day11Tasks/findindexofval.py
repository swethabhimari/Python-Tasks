import numpy as np
codes=[2,4,1,4,3,4,5]
arr=np.array(codes)
index_val=np.where(arr == 4)
print("index value where value=4:",index_val[0])
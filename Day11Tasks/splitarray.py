import numpy as np
std_scores=np.array([50,60,70,80,90,100,110,120])
split_array=np.array_split(std_scores,4)
print("split array into 4 parts:",split_array)
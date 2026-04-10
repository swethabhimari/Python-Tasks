import numpy as np
#random  matrix from 0-50
matrix=np.random.randint(0,51,(3,3))
print("matrix\n:",matrix)
#filter val>25
filter_val=matrix[matrix>25]
print("filtered:",filter_val)
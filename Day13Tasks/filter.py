import numpy as np
sales=np.array([12000,18000,9000,22000,15000,30000])
avg_val=np.mean(sales)
filtered_arr=sales[sales>avg_val]
print("average sales:",avg_val)
print("filtered array:",filtered_arr)
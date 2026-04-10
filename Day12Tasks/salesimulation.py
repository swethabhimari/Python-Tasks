import numpy as np
#ten random values between 100 -500
sales=np.random.randint(100,501,10)

print("random:",sales)
#avg sales
avg_sales=np.mean(sales)

print("average sales:",avg_sales)
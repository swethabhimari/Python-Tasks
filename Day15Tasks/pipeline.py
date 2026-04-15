import numpy as np
import pandas as pd
import time
#create file 
with open("nums.txt","w") as f:
    f.write("10\n20\n30\nabc\n40\n50\n")
#decorator for time calculation
def timer(func):
    def wrapper(*args):
        start = time.time()#start time
        result =func(*args)#call func
        end=time.time()#end time
        print("Time taken:",end - start)
        return result
    return wrapper
#generator to read file line by line
def read_numbers(file):
    with open(file) as f:
        for line in f:
            yield line.strip()
@timer#apply decorator
def process():
    nums=[]#empty list
#ead values using generator
    for val in read_numbers("nums.txt"):
        try:
            nums.append(float(val))
        except:
            print("Invalid:",val)
    arr = np.array(nums)#convert list to array
    mean = np.mean(arr)
    std = np.std(arr)#standard deviation
#store result in dataframe
    df = pd.DataFrame({"Mean":[mean],"Std":[std]})
    print(df)
process()


import random
nums=[]
#generate 10 random nums
for i in range(10):
    nums.append(random.randint(1,100))
even=0
odd=0
#count even/odd
for n in nums:
    if n % 2 == 0:
        even+=1
    else:
        odd+=1
#Remove duplicates
unique_nums=set(nums)
print("Numbers:",nums)
print("Even:",even)
print("Odd:",odd)
print("Unique:",unique_nums)
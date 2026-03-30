#check perfect
num = int(input("Enter anumber:"))
#find sum of proper divisions
sum_divisors=0
for i in range (1,num):
#condition
    if num% i==0:
        sum_divisors+=i
#check perfect 
if sum_divisors==num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
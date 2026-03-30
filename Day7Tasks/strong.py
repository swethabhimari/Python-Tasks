#Strong num number check
import math
num=int(input("Enter anumber:"))
digits=[int(d) for d in str(num)]
total = sum(math.factorial(d) for d in digits)

#conditioncheck
if total == num:
    print(f"{num} is a Strong Number")
else:
    print(f"{num} is not a strong number")
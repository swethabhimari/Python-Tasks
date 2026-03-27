from utilities import math_oper
from utilities import string_oper
a=int(input("Enter your first num:"))
b=int(input("Enter yoyr second num:"))

print("Addition:",math_oper.add(a,b))
print("Multiplication:",math_oper.mul(a,b))

#string operations
text=input("Enter a string:")
print("Uppercase:",string_oper.to_uppercase(text))
# print("Lowercase:",stropr.to_lowercase(text))
print("Character count:",string_oper.count_characters(text))
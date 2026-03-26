print("1.check positive negative,or zero")
num=float(input("enter a number:"))
if num > 0:
    print("given number is positive")
elif num < 0:
    print("given number is negative")
else:
    print("given number is zero")


print("2.Check voting eligibility")
age=int(input("enter your age:"))
if age >= 18:
    print("eligible to vote")
else:
    print("not eligible to vote")


print("3.largest of 3 nums")
num1=float(input("enter your first num:"))
num2=float(input("enter your second num:"))
num3=float(input("enter your third num:"))
if num1 >= num2 and num1>=num3:
    largest=num1
elif num2>=num1 and num2>=num3:
    largest=num2
else:
    largest=num3
print("The largest number is:",largest) 


print("4.check even or odd")
num=int(input("Enter a number:"))
if num%2==0:
    print("The number is even")
else:
    print("The number is odd")


print("5.assign grades based on marks")
marks=float(input("enter your marks:"))
if marks >= 90:
    grade="A"
elif marks >= 75:
    grade="B"
elif marks >= 50:
    grade="C"
elif marks > 35:
    grade="D"
else:
    grade="fail"
print("Your grade is:",grade)


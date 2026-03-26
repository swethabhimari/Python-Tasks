#1.
print(1.)
num1=int(input("enter the num:"))
num2=int(input("enter the num:"))
sum=num1+num2
print("sum=",sum)

#2.check if num is greater than other
print(2.)
a=int(input("enter any num1st:"))
b=int(input("enter any num 2nd:"))
if a>b:
    print(a,"is greater than ",b)
else:
    print(b,"is greater than",a)


#3.check even or odd
print("3.even or odd")
num=int(input("enter any num:"))
if num % 2==0:
    print(num,"is even")
else:
    print(num,"is odd")


#4.check age eligibility for voting using local operators
print(4.)
age=int(input("enter your age:"))
if age>=18:
    print("eligible for vote")
else:
    print("not eligible to vote")


#5.use of assignment operators
print(5.)
x=10
print("value:",x)
x+=5
print("x+5=",x)
x-=3
print("x-3=",x)


#comparision operators
print(6.)
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
print("a==b:",a==b)
print("a != b",a!=b)
print("a>b",a>b)
print("a<b",a<b)
print("a>=b",a>=b)
print("a<=b",a<=b)

#calculate power of a num
print(7.)
base=int(input("enter base:"))
exponent=int(input("enter exponent:"))

result=base ** exponent
print(base,"power of",exponent,"is",result)


#floor division operator
print(8.)
num1=int(input("enter numerator:"))
num2=int(input("enter denominator:"))
result=num1//num2
print("floor division rslt:",result)

#check 2 nums are equal
print(9.)
a=int(input("enter first num:"))
b=int(input("enter second num:"))
if a==b:
    print("nums are equal")
else:
    print("not equal")


#combine arithematic and comparision operators
print(10.)
a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))
if(a+b)>10:
    print("sum is greater than 10")
else:
    print("sum is 10  or less than 10")
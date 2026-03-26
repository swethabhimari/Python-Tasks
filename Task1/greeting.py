#1.greetings
print("1.GREETINGS")
name=input("Enter your name:")
print("Hello, " +name+ " Welcome to India")

#2.numbers
print("2.SUM OF NUMBERS")
num1=float(input("enter first number:"))
num2=int(input("enter second number:"))
sum_res=num1+num2
print("Total" ,sum_res)

#3.Age
print("3.AGE AFTER 5 YEARS")
age=int(input("enter person's age:"))
age_after_5years_=age+5
print("Your age after 5 years will be",age_after_5years_)

#4.print UPPERCASE
print("4.UPPER CASE")
sentence=input("Enter any sentence:")
print("Uppercase:",sentence.upper())

#5.print avg of numbers
print("5.PRINT AVG OF 3 NUMS")
n1=float(input("Enter 1st num:"))
n2=float(input("Enter 2st num:"))
n3=float(input("Enter 3st num:"))
avg = (n1+n2+n3)/3
print("Average of three nums:",avg)


#6.print square of a number
print("6.PRINT SQUARE OF A NUMBER")
num=float(input("enter any number:"))
square=num**2
print("square:",square)

#7.city name and msg
print("7.CITY NAME AND MSG")
city=input("enter your city name:")
print("You live in",city)

#8.product of 2 nums
print("8.PRODUCT OF 2 NUMS")
num1=float(input("enter 1st num:"))
num2=float(input("enter 2nd num:"))
product=num1 * num2
print("product:",product)

#9.print temperaure in C
print("9.PRINT TEMPERATURE")
temperature=float(input("Enter temp in celsius:"))
print("temperature:",temperature)

#10.display nput as sentence
print("10.DISPLAY INPUT AS SENTENCE")
name=input("enter your name:")
age=input("enter your age:")
print(name, "is" ,age, "years old." )
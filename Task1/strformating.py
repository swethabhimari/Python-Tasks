print("1.print name and age")
name="Swetha"
age=16
print("My name is %s and my age is %d" % (name,age))

print("2.format method")
name="swetha" 
age=16
print("My name is {} and my age is {}".format(name,age))


print("3.using f-strings")
name="swetha"
age=16
print("My name is {name} and my age is {age}")

print("4.float with 2 decimal places")
num=3.4567
print(f"value:{num:.2f}")

print("5.formatted prce value")
price=49.8
print(f"price:{price:.2f}")

print("6.sentence using 2 vars")
city="hyd"
country="India"
print("I live in {city},{country}.")

print("7.num with commas")
num=1000000
print(f"{num:,}")


print("8.display percentage")
marks=85
print(f"percentage:{marks}%")


print("9.align text L,R,center")
text="swetha"
print(f"left {text:<10}")
print(f"right{text:>10}")
print(f"center{text:^10}")


print("10.print a table row")
name="swetha"
age=16
marks=98.5
print(f"{name:<10} {age:<5} {marks:<10}") 
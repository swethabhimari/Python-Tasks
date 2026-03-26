def add(a,b):
    return a+b
x=int(input("Enter your first number:"))
y=int(input("Enter your second number:"))
print("Sum:",add(x,y))


def add(a=10,b=90):
    return a+b
print(add())
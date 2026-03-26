print("1.print num 1 to 10")
for i in range(1,11):
    print(i)


print("2.multiplication table of a num")
num=int(input("Enter a number:"))
for i in range(1,11):
    print(num,"x",i,"=",num*i)


print("3.sum of num 1 to n")
n=int(input("enter a numer n:"))
total=0
for i in range(1,n+1):
    total+=i
print("sum of num from 1 to ",n, "is",total)


print("4.print all even within 50")
for i in range(2,51,2):
    print(i,end=" ")
print()

print("5.factorial of num")
num=int(input("enter a num:"))
factorial =1
for i in range(1,num+1):
    factorial*=i
print("factorial of",num,"is",factorial)

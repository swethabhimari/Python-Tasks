print("stop print when reaches 5")
for i in range(1,11):
    if i == 5:
        break
    print(i)


print("2.skip printing num3 uing continue")
for i in range(1,11):
    if i == 3:
        continue
    print(i)


print("3.use pass inside a loop")
for i in range(1,11):
    if i == 3:
        pass
    print(i)


print("4.search for a num in list stop when found")
numbers=[1,2,3,4,5,6,7,8,]
search=int(input("Enter a number you want to serach:"))
for num in numbers:
    if num == search:
        print(search,"found in the list")
        break
else:
    print(search,"not found in the list")


print("print 1 to 10 but skip even")
for i in range(1,11):
    if i % 2 == 0:
        continue
    print(i)
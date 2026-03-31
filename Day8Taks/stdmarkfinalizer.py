#write students marks first
with open("marks.txt","w") as f:
    f.write("Swetha 98\nAnitha 90\nRavi 87\n")

#Students marks finalizer
total=0
count=0
with open("marks.txt","r") as f:
    print("Students Records:\n")

    for line in f:
        name,marks=line.split()
        marks=int(marks)
        print(name,marks)
        total+=marks
        count+=1
avg=total/count
print("\nAverage Marks:",avg),
#Grocery list manager
n = int(input("How many items?"))
#write data into file
with open("grocery.txt","w") as f:
    for i in range(n):
        item=input("Enter item name:")
        f.write(item+"\n")
print("Items saved successfully.")
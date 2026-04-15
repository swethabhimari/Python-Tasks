
cart=[]
#add items to cart
n=int(input("Enter number of items:"))
for i in range(n):
    item=input("Enter item name:")
    cart.append(item)

#remove duplicates
cart_set=set(cart)
total=0
#price calculation
for item in cart_set:
    try:
        price=float(input(f"Enter price of {item}:"))
        total+=price
    except:
        print("Invalid price!skipping.....")
print("Total cost:",total)
#Dictionary for product names and prices
products={
    "Pen":10,
    "Notebook":50,
    "Pencil":5
}
#set for product categories
categories={"Stationary"}
#List for cart items(each items as tuple:(product,quantity))
cart=[]
#func to display products
def display_products():
    print("Available products:")
    for product,price in products.items():
        print(f"{product}:{price}")
#Function to add item to cart
def add_to_cart():
    try:
        product_name=input("Enter product name:")
        if product_name not in products:
            raise NameError
        quantity=int(input("Enter quantity:"))
        #Tuple for product details
        item=(product_name,quantity)
        cart.append(item)
        print("Item added to cart successfully!")
    except ValueError:
        print("Invalid quantity!,Please enter a numeber.")
    except NameError:
        print("Product not found instore.")
    except TypeError:
        print("Cart data typr error.")
#   Recursive func to calculate total bill
def calculate_total(index=0):
    if index == len(cart):
        return 0
    try:
        product,quantity=cart[index]
        if not isinstance(quantity,int):
            raise TypeError
        return products[product]*quantity+calculate_total(index+1)
    except TypeError:
        print("Cart data tupe error.")
        return 0
#func to view total bill
def view_bill():
    try:
        if len(cart)==0:
            raise ZeroDivisionError
        print("Items in cart:")
        for product,quantity in cart:
            print(f"{product} x {quantity}")
        total = calculate_total()
        print("Total Bill:",total)
    except ZeroDivisionError:
        print("Calculation error")
    except TypeError:
        print("Cart data type error.")
#main
while True:
    print("\n1.Display products.")
    print("2.Add item to cart.")
    print("3.View total bill.")
    print("4.Exit.")

    choice = input("Enter choice:")  
    if choice == '1':
        display_products()
    elif choice=='2':
        add_to_cart()
    elif choice=='3':
        view_bill()
    elif choice=='4':
        print("Exit program.....")
    else:
        print("Invalid choice,Try again.")

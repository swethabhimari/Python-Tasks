#Multilevel inheritance-Online shopping sys
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class ElectronicProduct(Product):
    def __init__(self, name, price,warranty):
        Product.__init__(self,name,price)
        self.warranty=warranty
class MobilePhone(ElectronicProduct):
    def __init__(self, name, price, warranty,brand):
        ElectronicProduct.__init__(self,name, price, warranty)
        self.brand=brand
    def display(self):
        print(self.name,self.price,self.warranty,self.brand)
m=MobilePhone("Phone",20000,"1 year","SAMSUNG")
m.display()
        
        
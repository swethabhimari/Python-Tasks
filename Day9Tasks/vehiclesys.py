#Vehicle management sys-Inheritance
class Vehicle:
    def __init__(self,brand,speed):
        self.brand=brand
        self.speed=speed
class Car(Vehicle):
    def display(self):
        print("Car brand:",self.brand)
        print("Speed:",self.speed)

class Bike(Vehicle):
    def display(self):
        print("Bike brand:",self.brand)
        print("Bike speed:",self.speed)
c=Car("Toyota",120)
b=Bike("Yamaha",100)
c.display()
b.display()


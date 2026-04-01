#Shape area calculator -Polymorphism
class Circle:
    def area(self):
        r=3
        print("Area of circle:",3.14*r*r)
class Rectangle:
    def area(self):
        l,w=4,5
        print("Area of rectangle:",l*w)
class Triangle:
    def area(self):
        b,h=6,4
        print("Area of triangle:",0.5*b*h)
#Polymorphism
shapes=[Circle(),Rectangle(),Triangle()]
for s in shapes:
    s.area()
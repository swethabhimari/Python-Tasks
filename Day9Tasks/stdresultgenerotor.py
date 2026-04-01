#Student Result Generator-Method Overloading 
class Result:
    def calculate(self,m1,m2,m3=None):
        if m3 is None:
            total=m1+m2
        else:
            total=m1+m2+m3
        print("Total Marks:",total)
r=Result()
r.calculate(50,60)
r.calculate(50,60,70)
class Shape:
    def area(self):
        raise NotImplementedError
class Rectangle(Shape):
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius*self.radius
rec=Rectangle(5,2)
cir=Circle(5)
print("Area of rectangle:",rec.area())
print("Area of Circle:",cir.area())
class Rectangle():
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    def area(self):
        return self.l*self.b

length=int(input("Enter the value of length of the rectangle: "))
breadth=int(input("Enter the value of the breadth of the rectangle: "))
rect=Rectangle(length,breadth)
print("Area of the given rectangle is: ",rect.area())
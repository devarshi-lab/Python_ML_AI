class Circle:
    PI = 3.14
    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0
    
    def Accept(self,radius):
        self.Radius = radius
    
    def calculateArea(self):
        self.Area = Circle.PI*(self.Radius**2)
    
    def calcCircumference(self):
        self.Circumference = 2*(Circle.PI)*(self.Radius)
    
    def Display(self):
        print("Radius of circle is : ",self.Radius)
        print("Area of circle is : ",self.Area)
        print("Circumference of circle is : ",self.Circumference)
        print("-"*50)

def main():
    # radius = 0.0

    # try:
    #     radius = float(input("Enter the radius of circle : "))
    # except:
    #     print("Invalid Input.")

    circleObj = Circle()
    circleObj.Accept(5)
    circleObj.calculateArea()
    circleObj.calcCircumference()
    circleObj.Display()
    circleObj1 = Circle()
    circleObj1.Accept(8)
    circleObj1.calculateArea()
    circleObj1.calcCircumference()
    circleObj1.Display()
    circleObj2 = Circle()
    circleObj2.Accept(25.5)
    circleObj2.calculateArea()
    circleObj2.calcCircumference()
    circleObj2.Display()
    circleObj3 = Circle()
    circleObj3.Accept(15)
    circleObj3.calculateArea()
    circleObj3.calcCircumference()
    circleObj3.Display()
        

if __name__ == "__main__":
    main()


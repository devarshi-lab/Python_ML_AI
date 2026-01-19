# 2. Write a program which accepts radius of circle and prints area of circle.

PI = 3.14
def areaOfCircle(r):
    return PI*r*r

def main():
    radius = int(input("Enter radius : "))
    area = areaOfCircle(radius)
    print("Area of circle is : ",area)

if __name__ == "__main__":
    main()
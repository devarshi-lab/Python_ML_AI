# 1. Write a program which accepts length and width of rectangle and prints area.

def area(length,width):
    return length*width

def main():
    len = int(input("Enter length (meter) : "))
    wid = int(input("Enter width : (meter) "))
    areaRectangle = area(len,wid)
    print("Area of rectangle is : ",areaRectangle ," (sqmt)")
    # print(factor)

if __name__ == "__main__":
    main()
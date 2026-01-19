# 2. Write a lambda function which accepts one number and returns cube of that number.


getCube = lambda no : no**3

def main():
    value = int(input("Enter a number : "))
    cube = getCube(value)
    print("Cube of ",value," is : ",cube)

if __name__ == "__main__":
    main()
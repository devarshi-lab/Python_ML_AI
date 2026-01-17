# Write a program which accepts one number and prints cube of that number.

def cube(no):
    return no*no*no

def main():
    no = int(input("Enter the number : "))
    ret = cube(no)
    print("Cube of ",no," is : ",ret)

if __name__ == "__main__":
    main()

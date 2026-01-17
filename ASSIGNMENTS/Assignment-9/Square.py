# Write a program which accepts one number and prints square of that number.

def square(no):
    return no*no

def main():
    no = int(input("Enter the number : "))
    ret = square(no)
    print("Square of ",no," is : ",ret)

if __name__ == "__main__":
    main()

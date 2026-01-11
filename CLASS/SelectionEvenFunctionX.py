# Procedural Approach

def isEvenOdd(No):
    if (No % 2 == 1):
        print(No ," is Odd number")
    else :
        print(No , " is even number")

def main():
    no = 0
    no = int(input("Enter number : "))
    isEvenOdd(no)       # Positional Argument

if __name__ == "__main__":
    main()


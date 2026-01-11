#Procedural Approach 

def isEvenOdd(No):
    if (No % 2 == 1):
        print(No ," is Odd number")
    else :
        print(No , " is even number")

def main():
    no = 21
    isEvenOdd(no)       # Positional Argument
    isEvenOdd(No = no)  # Keyword Argument

if __name__ == "__main__":
    main()


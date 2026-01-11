# Procedural Approach

def isEvenOdd(No):
    if (No % 2 == 1):
        return False
    else :
        return True

def main():
    ans = False
    no = 0
    no = int(input("Enter number : "))
    ans = isEvenOdd(no)       # Positional Argument
    # print(ans)
    if (ans == True):
        print(no, " is even")
    else:
        print(no, " is odd")

if __name__ == "__main__":
    main()


# Procedural Approach

def isEvenOdd(No):
    return (No % 2 == 0)
       
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


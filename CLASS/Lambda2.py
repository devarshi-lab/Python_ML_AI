#Functional Approach

isEvenOdd = lambda No : No % 2 == 0


def main():
    value = 0
    ret = False
    value = int(input("Enter Number : "))
    ret = isEvenOdd(value)
    if (ret == True):
        print(value, " is even")
    else:
        print(value, " is odd")

if __name__ == "__main__":
    main()


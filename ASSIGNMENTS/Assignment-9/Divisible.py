# Write a program which accepts one number and checks whether it is divisible by 3 and 5

def isDivisibleBy3and5(no):
    if(no % 3 == 0 and no % 5 == 0):
        return True
    else :
        return False

def main():
    no = int(input("Enter the number : "))
    ret = isDivisibleBy3and5(no)
    if(ret):
        print(no , " is divisible by 3 and 5")
    else:
        print(no , " is not divisible by 3 and 5")

if __name__ == "__main__":
    main()
# Write a program which accepts one number and prints all odd numbers till that number.

def oddRange(no):
    odd = list()
    for i in range(1,no+1):
        if(i % 2 == 1):
            odd.append(i)
    return odd

def main():
    no = int(input("Enter the number : "))
    ret = oddRange(no)
    print("Odd number till  ",no," is : ",ret)

if __name__ == "__main__":
    main()
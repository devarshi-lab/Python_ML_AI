#  Write a program which accepts one number and prints its factors.

# Input: 12
# Output: 1 2 3 4 6 12

def factors(no):
    factarray = list()
    factarray.append(1)
    for i in range(2,no):
        if(no % i == 0):
            factarray.append(i)
    factarray.append(no)
    return factarray

def main():
    no = int(input("Enter number : "))
    factor = factors(no)
    print("Factors of ",no," is : ")
    print(factor)

if __name__ == "__main__":
    main()

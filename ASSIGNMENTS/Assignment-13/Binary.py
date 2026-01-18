# 4. Write a program which accepts one number and prints binary equivalent.

def binary(no):
    binary = ""
    while(no>0):
        binary += str(no % 2)
        no = int(no / 2) 
        # if(no % 2 == 0):
        #     binary += ("0")
        #     no = int(no / 2)
        # else:
        #     binary += ("1")
        #     no = int(no / 2)
    return (binary[::-1])

def main():
    no = int(input("Enter number : "))
    binaryNumber = binary(no)
    print("Binary equivalent of ",no, " is : ",binaryNumber)

if __name__ == "__main__":
    main()
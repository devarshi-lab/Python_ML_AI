# Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output:
# 4 8 12 16 20 24 28 32 36 40

def table(no):
    tableValues = list()
    for i in range(1,11):
        tableValues.append(no*i)
    
    return tableValues

def main():
    no = int(input("Enter the number : "))
    ret = table(no)
    print("Table of ",no ," : \n",ret)

if __name__ == "__main__":
    main()

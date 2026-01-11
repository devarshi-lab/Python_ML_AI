def main():
    size = 0
    value  = 0
    print("Enter the no. of elements : ")
    size = int(input())

    Data = list()

    print("Enter the elements : ")
    for i in range(size):
        value = int(input())
        # Data[i] = value   # error
        Data.append(value)

    sum = 0

    for i in range(size):
        sum = sum + Data[i]
    
    print("SUmmation is : ",sum)

if __name__ == "__main__":
    main()
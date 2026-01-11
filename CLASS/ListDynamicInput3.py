def summation(elements):
    sum = 0
    for i in range(len(elements)):
        sum = sum + elements[i]
    return sum
    
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

    sum = summation(Data)
    print("SUmmation is : ",sum)

if __name__ == "__main__":
    main()
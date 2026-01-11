def checkEven(No):
    return No % 2 == 0

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)
    
    Fdata = list(filter(checkEven,Data))
    print("Data after filter : ",Fdata)


if __name__ == "__main__" :
    main()
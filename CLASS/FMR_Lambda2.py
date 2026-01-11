from functools import reduce

def main():
    Data = [11,10,15,20,22,27,30]
    print("Actual Data is : ",Data)
    
    Fdata = list(filter((lambda No : (No % 2 == 0)),Data))
    print("Data after filter : ",Fdata)

    Mdata = list(map((lambda No : (No+1)),Fdata))
    print("Data after map : ",Mdata)

    Rdata = int(reduce((lambda a,b : a+b),Mdata))
    print("Data after reduce : ",Rdata)

if __name__ == "__main__" :
    main()
#Input :    multiple parameters 
#Output : One Value
def Marvellous1(value1,value2):
    print("Inside Marvellous1 : ", value1 , value2)
    return 21

def main():
    ret = None
    ret = Marvellous1("python",31)
    print("Return Value is : " , ret)

if __name__ == "__main__":
    main()
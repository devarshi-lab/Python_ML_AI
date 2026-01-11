#Input :    multiple parameters 
#Output : multiple values
def Marvellous1(value1,value2):
    print("Inside Marvellous1 : ", value1 , value2)
    return 11,21,31

def main():
    ret1 = None
    ret2 = None
    ret3 = None
    ret1,ret2,ret3 = Marvellous1("python",31)
    print("Return Values are : ", ret1, ret2,ret3)

if __name__ == "__main__":
    main()
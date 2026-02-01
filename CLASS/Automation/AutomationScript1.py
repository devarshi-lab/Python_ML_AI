import sys
def main():
    Border = "-"*50
    print(Border)
    print("--------------- Marvellous Automation-------------")
    print(Border)

    if(len(sys.argv)==2):
        if((sys.argv[1])=="--h" or (sys.argv[1])=="--H"):
            print("This application is used to perform _________")
            print("This is a automation script")
        elif((sys.argv[1])=="--u" or (sys.argv[1])=="--U"):
            print("Use the given script as ")
            print("Scriptname.py argument1 argument 2")
            print("argument1 : __________________")
            print("argument2 : __________________")
        else:
            print("Use the given flags as : ")
            print("--u : use to display the usage")
            print("--h : use to display the help")
    else:
        print("Invalid number of command line arguments")
        print("Use the given flags as : ")
        print("--u : use to display the usage")
        print("--h : use to display the help")

    print(Border)
    print("-----------Thank You for using our script----------")
    print("--------------- Marvellous Infosystems-------------")
    print(Border)

if __name__ == "__main__":
    main()
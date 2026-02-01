# python commandline4.py 11 10
import sys 

def main():
    if(len(sys.argv)!=3):
        print("Required only two command line parameters")
        return
    
    print("Addition is : " ,int(sys.argv[1]) + int(sys.argv[2]))

if __name__ == "__main__":
    main()
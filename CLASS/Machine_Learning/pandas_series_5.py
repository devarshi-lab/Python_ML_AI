import pandas as pd

def main():
    Data = [11,21,51,101,111]

    print(Data)
    
    sobj = pd.Series([25000,27000,29000,30000],index=["PPA","LB","PYTHON","REACT"])

    print(sobj)

    print(sobj["PYTHON"])

if __name__ == "__main__":
    main()
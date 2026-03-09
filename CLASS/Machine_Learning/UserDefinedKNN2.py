# [A,B,C,D]
# X[1,2,3,5]
# Y[2,3,1,6]
#  [R,R,B,B]

# Predict (3,3) => ?

import numpy as np
import math

def EucDistance(P1,P2):
    Ans = math.sqrt(((P1['X']-P2['X'])**2) + ((P1['Y']-P2['Y'])**2))
    return Ans

def MarvellousKNeighboursClassifier():
    border = "-"*50
    data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':5,'Y':6,'label':'Blue'}
        ]
    
    print(border)
    print("Marvellous User Defined KNN")
    print(border)
    print(border)
    print("Training Dataset")
    print(border)
    for i in data:
        print(i)

    print(border)
    new_point = {'X':3,'Y':3}

    print(data[0])
    print(new_point)

    print(border)
    result = EucDistance(data[0],new_point)

    print(result)

def main():
    MarvellousKNeighboursClassifier()

if __name__ == "__main__":
    main()
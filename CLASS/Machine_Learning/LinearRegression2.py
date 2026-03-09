import numpy as np
import math
import pandas as pd
import matplotlib.pyplot as plt

def MarvellousPredictor():
    border = "-"*50
    # Load the data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    print("Values of independent variables : ", X)    
    print("Values of dependent variables : ", Y)

    mean_x = np.mean(X)
    mean_y = np.mean(Y)
    print(border)
    print("Mean of X is : ",mean_x) # 3.0
    print("Mean of Y is : ",mean_y) # 3.6

    n = len(X) # 5

    # Y = mX + c

    # m = (summation (X-Xbar) * (Y-Ybar)) / (summation (X- Xbar) ** 2)

    numerator = 0
    denominator = 0

    for i in range(n):
        numerator = numerator + ((X[i]-mean_x )*(Y[i]-mean_y))
        denominator = denominator + ((X[i]-mean_x)**2)
    
    m = numerator / denominator

    print("Value of m (Slope of line) is : ",m) # 0.4

    c = mean_y - (m * mean_x)

    print("Y-intercept of line i.e. C is : ",c)


def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()
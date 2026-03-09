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
    print("Mean of X is : ",mean_x)
    print("Mean of Y is : ",mean_y)

def main():
    MarvellousPredictor()

if __name__ == "__main__":
    main()
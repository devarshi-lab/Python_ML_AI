
def main():
    Dataset = [
        {"X":1,"Y":3},
        {"X":2,"Y":4},
        {"X":3,"Y":2},
        {"X":4,"Y":4},
        {"X":5,"Y":5},
    ]

    sumX = 0
    sumY = 0
    XMean = 0
    YMean = 0
    for data in Dataset:
        sumX = sumX + data["X"]
        sumY = sumY + data["Y"]

    XMean = sumX / len(Dataset)
    YMean = sumY / len(Dataset)
    
    # print("X Mean: ", XMean)
    # print("Y Mean: ", YMean)

    xminusXMeanintoyminusYMean = 0
    xminusXMeanSquare = 0
    xminusXMean = 0
    yminusYMean = 0
    for data in Dataset:
        xminusXMean = data["X"] - XMean
        data["xminusXMean"] = xminusXMean
        yminusYMean = data["Y"] - YMean
        data["yminusYMean"] = yminusYMean
        xminusXMeanintoyminusYMean = xminusXMeanintoyminusYMean + (xminusXMean * yminusYMean)
        xminusXMeanSquare = xminusXMeanSquare + (xminusXMean * xminusXMean)
    
    # print("xminusXMeanSquare: ", xminusXMeanSquare)
    # print("xminusXMean: ", xminusXMean)
    # print("yminusYMean: ", yminusYMean)
    # print("xminusXMeanintoyminusYMean: ", xminusXMeanintoyminusYMean)
    m =xminusXMeanintoyminusYMean / xminusXMeanSquare
    c = YMean - (m * XMean)


    labelFormat = "{:<18} {:<18} {:<18} {:<18} {:<18} {:<18}"
    numformat = "{:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f}"
    print(labelFormat.format("X", "Y", "x-xmean", "y-ymean", "(x-xmean)(y-ymean)", "(x-xmean)^2"))
    for data in Dataset:
        print(numformat.format(data["X"], data["Y"], data["xminusXMean"], data["yminusYMean"], (data["xminusXMean"] * data["yminusYMean"]), (data["xminusXMean"] * data["xminusXMean"])))
    
    print("-" * 108)
    print(labelFormat.format("Xbar = " + str(XMean), "Ybar = " + str(YMean), "", "", "Sum = " + str(xminusXMeanintoyminusYMean), "Sum = " + str(xminusXMeanSquare)))
    print("-" * 108)

    print("m (slope) : ", m)
    print("c (y-intercept) : ", c)

    inputX = 6
    predictedY = (m * inputX) + c
    print("-" * 108)
    print("Predicted Y for X = 6 : ", predictedY)


if __name__ == "__main__":
    main()
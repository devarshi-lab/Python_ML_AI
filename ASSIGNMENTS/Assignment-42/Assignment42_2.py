import json 

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

    # m (slope) : (Σ((x-xbar)(y-ybar))) / Σ((x-xbar)^2))
    m =xminusXMeanintoyminusYMean / xminusXMeanSquare

    # c (y-intercept) : ybar - (m * xbar)
    c = YMean - (m * XMean)

    SummationYpminusYMeanSquare = 0
    SummationYminusYMeanSquare = 0
    SummationYminusYp = 0
    SummationYminusYpSquare = 0
    labelFormat = "{:<12} {:<12} {:<12} {:<12} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18} {:<18}"
    numformat = "{:<12.2f} {:<12.2f} {:<12.2f} {:<12.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f} {:<18.2f}"
    print(labelFormat.format("X", "Y", "x-xbar", "y-ybar", "(x-xbar)(y-ybar)", "(x-xbar)^2","(y-ybar)^2", "Yp", "Yp-Ybar", "(Yp-Ybar)^2", "Y-Yp", "(Y-Yp)^2"))
    for data in Dataset:
        data["yminusYMeanSquare"] = data["yminusYMean"] * data["yminusYMean"]
        SummationYminusYMeanSquare = SummationYminusYMeanSquare + data["yminusYMeanSquare"]

        data["Ypredicted"] = (m * data["X"]) + c 
        data["YpminusYMean"] = data["Ypredicted"] - YMean

        data["YpminusYMeanSquare"] = data["YpminusYMean"] * data["YpminusYMean"]
        SummationYpminusYMeanSquare = SummationYpminusYMeanSquare + data["YpminusYMeanSquare"]

        data["YminusYpredicted"] = (data["Y"] - data["Ypredicted"])
        SummationYminusYp = (SummationYminusYp + data["YminusYpredicted"])

        data["YminusYpredictedSquare"] = data["YminusYpredicted"] * data["YminusYpredicted"]
        SummationYminusYpSquare = SummationYminusYpSquare + data["YminusYpredictedSquare"]

        print(numformat.format(data["X"], data["Y"], data["xminusXMean"], data["yminusYMean"], (data["xminusXMean"] * data["yminusYMean"]), (data["xminusXMean"] * data["xminusXMean"]), data["yminusYMeanSquare"], data["Ypredicted"], data["YpminusYMean"], data["YpminusYMeanSquare"],data["YminusYpredicted"],data["YminusYpredictedSquare"]))


    print("-" *216)
    print(labelFormat.format("Xbar = " + str(XMean), "Ybar = " + str(YMean), "", "", "Σ = " + str(xminusXMeanintoyminusYMean), "Σ = " + str(xminusXMeanSquare), "Σ = " + str(SummationYminusYMeanSquare),"","", "Σ = " + str(round(SummationYpminusYMeanSquare, 2)),"","Σ = " + str(round(SummationYminusYpSquare, 2))))
    print("-" * 216)

    print("m (slope) : ", m)
    print("c (y-intercept) : ", c)

    print("-" * 216)

    # R^2 Score : (Σ((Yp-Ybar)^2)) / Σ((Y-Ybar)^2))
    R_score = SummationYpminusYMeanSquare / SummationYminusYMeanSquare
    print("R^2 Score : ", R_score)

    # MSE : (Σ((Y-Yp)^2)) / n

    MSE = SummationYminusYpSquare / len(Dataset)
    print("MSE : ", MSE)




if __name__ == "__main__":
    main()
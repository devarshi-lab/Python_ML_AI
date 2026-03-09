from sklearn.metrics import confusion_matrix
def main():
    # 1 : Positive
    # 0 : Negative

    actual = [1,0,1,1,1,0,1,0,0,1]
    predicted = [1,0,0,1,1,1,1,1,0,1]

    print("Actual Data : ",actual)
    print("Predicted Data : ",predicted)


    con_mat = confusion_matrix(actual,predicted)
    print(con_mat)

if __name__ == "__main__":
    main()
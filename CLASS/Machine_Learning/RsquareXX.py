from sklearn.metrics import r2_score

def main():
    y_actual = [3,4,2,4,5]          # Y
    y_pred = [3,4,2,4,5]  # Yp

    r2 = r2_score(y_actual,y_pred)

    print("Actual values : Y ",y_actual)
    print("Predectied values : Yp ",y_pred)
    print("R square value : ",r2) # 1.0



if __name__ == "__main__":
    main()
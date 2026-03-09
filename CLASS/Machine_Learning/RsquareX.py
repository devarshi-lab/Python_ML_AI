from sklearn.metrics import r2_score

def main():
    y_actual = [3,4,2,4,5]          # Y
    y_pred = [1.8,1.2,3.6,1.0,2.4]  # Yp

    r2 = r2_score(y_actual,y_pred)

    print("Actual values : Y ",y_actual)
    print("Predectied values : Yp ",y_pred)
    print("R square value : ",r2) 



if __name__ == "__main__":
    main()
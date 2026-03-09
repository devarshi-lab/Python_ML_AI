import math

def main():
    Point = ['A', 'B', 'C', 'D']
    X = [1,2,3,6]
    Y = [2,3,1,5]
    Label = ["Red","Red","Blue","Blue"]

    inputX = int(input("Enter the value of X : "))
    inputY = int(input("Enter the value of Y : "))

    Distances = {}
    for i in range(len(X)):
        # Euclidean Distance
        distance = math.sqrt((X[i] - inputX)**2 + (Y[i] - inputY)**2)
        Distances[Point[i]] = {
            "Distance": distance,
            "Label": Label[i]
        }
    
    Distances = sorted(Distances.items(), key=lambda x: x[1]["Distance"])[:3]
    print(Distances)
    print("Nearest Neighbours")
    classification = {}
    for point, distance in Distances:
        print(f"Distance from {point} : {distance}")
        label = distance["Label"]
        if label in classification:
            classification[label] += 1
        else:
            classification[label] = 1

    print("Classification : ", classification)
    predicted_label = max(classification, key=classification.get)
    print("Predicted Class : ", predicted_label)

if __name__ == "__main__":
    main()
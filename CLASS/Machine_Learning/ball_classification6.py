# Steps for machine learning applications

# Step 1 : Data Gathering / Collection
# Step 2 : Data analysis
# Step 3 : Data cleaning
# Step 4 : Model Selection
# Step 5 : Model Training
# Step 6 : Model Testing / Evaluation
# Step 7 : Model Improvement 
# Step 8 : Prediction / Deployment

from sklearn import tree


def main():
    print("Ball Classification Case Study")

    # Data Loading / Gathering 

    # Feature Encoding 
    # Rough = 1
    # Smooth = 0

    # Original Encoded Dataset
    # Independent Variables
    X = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 

    # Independent variables for training 
    Xtrain = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0]] 
    
    # Independent variables for testing 
    Xtest = [[35,1],[95,0]]

    # Dependent variables for training
    Ytrain = [1,1,2,1,2,1,2,1,1,1,2,1,2]

    # Dependent variables for testing
    Ytest = [1,2]

    # Label Encoding
    # Tennis = 1
    # Cricket = 2

    # Dependent Variables
    Y = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelObj = tree.DecisionTreeClassifier()

    trainedModel = modelObj.fit(Xtrain,Ytrain)

    result = trainedModel.predict([[35,1]])

    print(type(result))

    if result == 1:
        print("Object looks like tennis ball")
    elif result == 2:
        print("Object looks like cricket ball")
    

    # print("Model predicts the object as : ",result)
    
    

if __name__ == "__main__":
    main()


# Dataset Size : 15

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

    # Independent Variables
    Features = [[35,1],[47,1],[90,0],[48,1],[90,0],[35,1],[92,0],[35,1],[35,1],[35,1],[96,0],[43,1],[110,0],[35,1],[95,0]] 

    # Label Encoding
    # Tennis = 1
    # Cricket = 2

    # Dependent Variables
    Labels = [1,1,2,1,2,1,2,1,1,1,2,1,2,1,2]

    modelObj = tree.DecisionTreeClassifier()

    trainedModel = modelObj.fit(Features,Labels)

    result = trainedModel.predict([[37,1],[94,0]]) # [1 2]

    print("Model predicts the object as : ",result)
    
    

if __name__ == "__main__":
    main()


# Dataset Size : 15

from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")

    Dataset = load_iris()
    # Metadata of datasets
    print("Independent Variable are : ")
    print(Dataset.feature_names)
    
    print("Dependent Variable are : ")
    print(Dataset.target_names)

if __name__ == "__main__":
    main()
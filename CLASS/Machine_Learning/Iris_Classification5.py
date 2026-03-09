from sklearn.datasets import load_iris

def main():
    print("Iris Classification Case Study")
    border = "-"*50

    Dataset = load_iris()
    print(border)

    for i in range(len(Dataset.target)):
        print("ID %d, Features %s, Label %s" %(i,Dataset.data[i],Dataset.target[i]))
        
if __name__ == "__main__":
    main()
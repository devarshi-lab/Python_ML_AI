import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Data = [10,20,30,20,20,20,30,40]
    # Categorical Data
    # sns.countplot(x=["A","B","B","A","A","A","C"])
    sns.countplot(x=Data)

    plt.show()

if __name__ == "__main__":
    main()
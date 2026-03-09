import matplotlib.pyplot as plt
import seaborn as sns

def main():
    Data = [10,20,30,20,20,20,30,40]
    
    sns.countplot(x=["C","C","C++","Java","C++","Python","Javascript","C++","GoLang","C"])

    plt.show()

if __name__ == "__main__":
    main()
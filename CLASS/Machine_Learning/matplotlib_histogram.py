import matplotlib.pyplot as plt
import seaborn as sns

def main():
    # Contigues values
    Data = [10,20,30,20,20,20,30,40]
    
    sns.histplot(data=Data)

    plt.show()

if __name__ == "__main__":
    main()
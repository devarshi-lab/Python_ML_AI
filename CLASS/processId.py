import os

def main():
    print("pid of running process is : ",os.getpid())
    print("pid of parent process is: ",os.getppid())
if __name__ == "__main__":
    main()
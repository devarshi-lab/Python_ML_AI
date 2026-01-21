def Fun():
    """
   1.Write a program which contains one function named as Fun(). That function should display “Hello from Fun” on console.
    """
    print("Hello from Fun")

def main():
    print(Fun.__doc__)
    Fun()

if __name__ == "__main__":
    main()
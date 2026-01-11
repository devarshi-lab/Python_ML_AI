
def outer():
    print("Inside Outer")
    
    def inner():
        print("Inside Inner")
    
    inner()


def main():
    outer()


if __name__ == "__main__":
    main()
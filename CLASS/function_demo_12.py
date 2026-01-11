
def outer():
    print("Inside Outer")
    
    def inner():
        print("Inside Inner")


def main():
    outer.inner()


if __name__ == "__main__":
    main()
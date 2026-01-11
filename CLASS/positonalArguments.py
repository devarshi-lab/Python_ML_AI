def Display(a,b,c,d):
    print(a,b,c,d)

def main():
    # Display(1,2) Not Allowed - less arguments
    # Display(1,2,3,4,5) Not Allowed - Extra arguments
    Display(1,2,3,4) # Allowed 

if __name__ == "__main__":
    main()
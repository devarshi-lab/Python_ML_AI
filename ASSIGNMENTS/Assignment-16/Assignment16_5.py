def main():
    """5.Write a program which display 10 to 1 on screen.
Output : 10 9 8 7 6 5 4 3 2 1"""
    print(main.__doc__,"\n\n",("-"*50),"\n\n")
    for i in range(10,0,-1):
        print(i,end="\t")

if __name__ == "__main__":
    main()
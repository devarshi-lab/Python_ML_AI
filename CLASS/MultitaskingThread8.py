import threading

def Display(no):
    print("Inside Display : ",no)


def main():
    t = threading.Thread(target=Display, args=(11,))
    t.start()

if __name__ == "__main__":
    main()
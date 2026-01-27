class BookStore:
    NoofBooks = 0

    def __init__(self,Name,Author):
        self.Name = Name
        self.Author = Author
        BookStore.NoofBooks += 1
    
    def Display(self):
        print(f"{self.Name} by {self.Author}")
        print("No. of Books : ",BookStore.NoofBooks)

def main():
    bookObj = BookStore("Chhava","Shivaji Savant")
    bookObj.Display()
    bookObj2 = BookStore("C Programming","Dennis Ritchie")
    bookObj2.Display()

if __name__ == "__main__":
    main()

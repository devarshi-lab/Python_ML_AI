class BankAccount:
    ROI  = 10.5
    def __init__(self,Name,Amount):
        self.Name = Name
        self.Amount = Amount
    
    def Display(self):
        print(f"Account Holder : {self.Name}")
        print(f"Current Balance : {self.Amount}")
        print("*"*50)
    
    def Deposit(self,amount):
        print(f"Depositing amount {amount} to account holder {self.Name}")
        self.Amount  += amount
    
    def Withdraw(self,amount):
        print(f"Withdrawing amount {amount} from account holder {self.Name}")
        if(amount>self.Amount):
            print("Insufficient Balance")
        else:
            self.Amount  -= amount
    
    def CalculateInterest(self):
        return (self.Amount*BankAccount.ROI) / 100
    
def main():
    bankAcc1 = BankAccount("ABC",10000)
    bankAcc1.Display()
    bankAcc2 = BankAccount("XYZ",50000)
    bankAcc2.Display()
    bankAcc3 = BankAccount("PQR",3500)
    bankAcc3.Display()

    bankAcc1.Deposit(25000)
    bankAcc1.Display()

    bankAcc2.Withdraw(5000)
    bankAcc2.Display()

    bankAcc3.Withdraw(500)
    bankAcc3.Display()

    print("Interest on amount is : ", bankAcc2.CalculateInterest())
    bankAcc2.Display()

    bankAcc3.Withdraw(5000)
    bankAcc3.Display()


if __name__ == "__main__":
    main()



        
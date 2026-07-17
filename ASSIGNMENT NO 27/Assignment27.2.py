class BankAccount:
    ROI=10.5

    
    def __init__(self , Name , Amount):
        self.Name =  Name
        self.Amount = Amount
        
    def Display(self):
        print("Account Holder Name is:",self.Name)
        print("Balance is :",self.Amount)

    def Deposite(self):
        Money = float(input("Enter the Amount to Deposite:"))
        self.Amount = self.Amount +Money
        print("Amount Deposite Succesfully")

    def Withdraw(self):
        Money = float(input("Enter the Amount to withdraw:"))

        if Money<=self.Amount:

            self.Amount = self.Amount - Money
            print("Amount withdraw succesfully")
        else:
            print("Balance is insufficient")

    def CalculateInterest(self):
        Interest =(self.Amount *BankAccount.ROI)/100
        print("Interest is:", Interest)

def main():
    Name = input("Enter Account Holder Nmae:")
    Amount = float(input("Enter initial balance:"))

    obj1 = BankAccount(Name , Amount)
    obj2 = BankAccount(Name , Amount)

    obj1.Display()
    obj1.Deposite()
    obj1.Display()

    obj1.Withdraw()
    obj1.Display()

    obj1.CalculateInterest()
    print("-----------------------------------")

      
    obj2.Display()
    obj2.Deposite()
    obj2.Display()

    obj2.Withdraw()
    obj2.Display()

    obj2.CalculateInterest()

if __name__ == "__main__":
    main()

class BankAccount:
    
    def __init__(self):
        self.balance=0
    
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance

    def withdrawal(self,amount):
        #print(self.balance)
            self.balance=self.balance-amount
            return self.balance

class SavingsAccount(BankAccount):

    def __init__(self):
        super().__init__()
        
    
    def operate(self):
        while True:
            print("Welcome to the bank system:")
            print("do you wish to:") 
            print("1.deposit")
            self.action=int(input("2.withdraw: "))
            #print(self.action)
            
            if self.action==1:
                self.amount=int(input("Enter the amount you want deposit: "))
                self.deposit(self.amount)
                print("The deposit has been made")
                print("balance:", self.balance)
                print("----"*20)
                input("Press enter to return to menu")

            if self.action==2:
                self.min_balance=100
                second_balance=0
                #print(self.balance)
                while True:
                    self.amount=int(input("Enter the amount you want withdraw:"))
                    second_balance=self.balance-self.amount
                    if second_balance<self.min_balance:
                        #print(second_balance)
                        print("The balance can't be fewer than", self.min_balance, "please withdraw another amount")
                    elif second_balance>=self.min_balance:
                        self.withdrawal(self.amount)
                        print("You have withdrawed",self.amount,"from your account")
                        print("balance:",self.balance)
                        print("----"*20)
                        input("Press enter to return to menu")
                        break
            yes=input("Do you wish to make another movement?:(Y/N):")
            if yes=="N" or yes=="n":
                print("Thank you for using our bank services")
                print("----"*20)
                break

saving1=SavingsAccount()

saving1.operate()
    
class Client:

    def __init__(self,name,amount):
        self.name=name
        self.amount=amount

    def __add__(self, object2):
        s=self.amount+object2.amount
        return s
    
#main
client1=Client("Amanda", 200)
client2=Client("Luis",300)
print("total amount in bank account")
print(client1+client2)
        
class Player:

    name="Louis"
    score=10
    counter=30

    def __init__(self):
        pass

    def printing(self):
        pass

    def passing_time(self):
        while self.counter>0:
            print(self.counter, "seconds are left")
            self.counter-=1


#main
player1=Player()
player2=Player()

print("Player1:")
player1.passing_time()
input("press enter to continue with next player")
print("Player2:")
player2.passing_time()



number=0
import random
random=random.randint(1,10)
while number!=random:
        number=int(input("enter the number:"))
        if number!=random:
            print("try again")
        if random==number:
            print("you guessed right")

number_1=int(input("enter the first number:"))
number_2=int(input("enter the second number:"))
number_3=int(input("enter the third number"))

if number_1>number_2 and number_1>number_3:
    print(number_1,"is the biggest")
elif number_2>number_3:
    print(number_2, "is the biggest")
else:
    print(number_3,"is the biggest")

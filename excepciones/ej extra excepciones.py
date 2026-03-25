def ask():
    x=0
    while x<100:   
        try:
            name=input("please enter a name:")
            if name.isdigit():
                raise ValueError
        except ValueError as error:
            print("ValueError: enter a valid digit", error)
        try:
                age=int(input("enter the age:"))
                print("Hola",name,", your age is ",age)
                return (name,age)
        except ValueError as error:
                print("ValueError: enter a valid digit", error)
        x +=1
    

#bloque principal
ask()
    
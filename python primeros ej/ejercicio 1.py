name=input("enter your name:")
second_name=input("enter your last name:")
age=int(input("enter your age:"))
if age<3:
    print("es un bebe")
elif age<10:
    print("es un niño")
elif age<13:
    print("es un preadolescente")
elif age<20:
    print("es un adolescente")
elif age<30:
    print("es un joven")
elif age<40:
            print("es un adulto joven")
elif age<65:
     print("es un adulto")
elif age>65:
     print("es un adulto mayor")
def summ_values(list2):
    summ=0
    for x in range(len(list2)):
        summ=summ+list2[x]
        print(list2[x],"added correctly!")
    print("total summ:", summ)

def listing():
    list1=[]
    list2=[]
    element=0
    for x in range(5):
        element=input("enter the element to add:")
        list1.append(element)
        try:
            convert=float(list1[x])
            list2.append(convert)
        except ValueError:
            print(list1[x],": ValueError: invalid element")
    print(list2)
    return list2

#bloque principal
list2=[]
list2=listing()
summ_values(list2)

def list1(word):
    list1=[]
    summ=""
    for item in word:
        if item!="-":
            summ=summ+item
        else:
            list1.append(summ)
            summ=""
    list1.append(summ)
    return(list1)

def ordenar(list1):
    list2=sorted(list1)
    return(list2)
    
def convertir(list2):
    new_word=list2[0]
    for x in range(1,len(list2)):
        new_word=new_word+"-"+list2[x]
    return(new_word)


#bloque principal
word=input("enter the words separated by -:")
list1=list1(word)
print(list1)
list2=ordenar(list1)
print(list2)
print(convertir(list2))



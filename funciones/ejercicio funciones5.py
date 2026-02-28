def suma():
    lista1=[10,15,5,12,32]
    sum=0
    for item in range(len(lista1)):
        sum += lista1[item]
    return sum


#bloque principal
valor=0
valor=suma()
print(valor)
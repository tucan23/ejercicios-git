valor=int(input("ingrese el valor a sumar"))

def funcion_suma(valor):
    suma=10
    suma += valor 
    return suma


#bloque principal
suma=funcion_suma(valor)
print(suma)
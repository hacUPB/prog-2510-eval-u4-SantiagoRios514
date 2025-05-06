#filas = 2
#columnas = 3
#Lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
#for i in range(filas):        #Número de filas que tendrá la matriz (4)
#    Lista.append([])      #Agregamos una fila vacía a la matriz
#    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
#        n = int(input("Ingrese un valor: "))
#        Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente
#print(Lista)

from random import randint
filas = 5
columnas = 12
ventas_ano = []
Lista = []                #Creamos una lista vacía [[6,8,67],[4,7,12]]
for i in range(filas):        #Número de filas que tendrá la matriz (4)
    Lista.append([])      #Agregamos una fila vacía a la matriz
    for j in range(columnas):    #En este bucle vamos a recorrer cada una de las filas (3)
        n = randint(0, 30)
        Lista[i].append(n)  #Agregamos un elemento a la Lista en la posición siguiente

for i in range(filas):
    for j in range(columnas):
        print(f"{Lista[i][j]:4}", end='  ')
    print()

for i in range(filas):
    suma = sum(Lista[i])
    ventas_ano.append(suma)

print(ventas_ano)
mayor = max(ventas_ano)
indice = ventas_ano.index(mayor)
print(f"El año de mayor ventas fue {2020+indice}, se vendieron {mayor} carros.")
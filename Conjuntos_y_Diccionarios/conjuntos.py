from random import randint

lista1 = []
lista2 = []
for i in range(100):
    lista1.append(randint(0,100))
    lista2.append(randint(50,150))

conjunto1 = set(lista1)
conjunto2 = set(lista2)

# Encontrar los elementos comunes:
comunes = conjunto1.intersection(conjunto2)
print(f"Comunes: {comunes}")

# Encontrar los elementos no comunes:
noComunes = conjunto1.symmetric_difference(conjunto2)
print(f"No comunes: {noComunes}")
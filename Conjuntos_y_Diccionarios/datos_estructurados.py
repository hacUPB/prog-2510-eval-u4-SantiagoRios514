usuarios = {
    "user1": {"nombre": "Ana", "edad": 25},
    "user2": {"nombre": "Luis", "edad": 30}
}

print(usuarios["user1"]["edad"])

# Pedir los datos al usuario y agregarlo al diccionario:
nombre = input("Ingrese su nombre: ")
edad = input("Ingrese su edad: ")
user3 = {}
user3["nombre"] = nombre
user3["edad"] = edad

usuarios["user3"] = user3

print(usuarios)
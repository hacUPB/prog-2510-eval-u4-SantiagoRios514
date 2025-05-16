nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
cedula = input("Ingrese su cédula: ")
# Abrir un archivo, Crear un archivo en el escritorio

var_archivo = open("C:\\Users\\B09S202est\\Desktop\\Texto1.txt","a")
var_archivo.write(f"{nombre} con cédula {cedula} tiene {edad} años\n")

# Cerrar el archivo

var_archivo.close()
# Importar librerías
import os                       # Listar archivos

# Importar funciones propias
import archivo_txt as txt       # Trabajar con archivos de texto
import archivo_csv as csvf      # Trabajar con archivos CSV

print('-'*40)
print("Análisis de datos en .CSV y .TXT")
print('-'*40)

# Solicitar la ruta de la carpeta
# Verificar si la ruta termina con '/' y agregarlo si no lo tiene
ruta = input("\nIngrese la ruta de la carpeta: ")
if not ruta.endswith('/'):
    ruta += '/'

# Menú principal
print("L. Listar archivos en la ruta actual\nT. Procesar archivo de texto (.txt)\nC. Procesar archivo separado por comas (.csv)\nS. Salir")
menu = input("Escoja la opción que quiere (L, T, C, S): ").upper()

match menu:
    case 'L': # Listar archivos
        ruta_completa = os.path.abspath(ruta) # Obtener la ruta completa
        print(f"\nArchivos en la ruta: {ruta_completa}") # Lista el directorio
        print('-'*40)
        # Listar archivos en la ruta
        for archivo in os.listdir(ruta):
            print(archivo)
    case 'T': # Procesar archivo de texto
        print("\n")
        print('-'*40)
        print("Submenú de archivos de texto")
        print('-'*40)

        # Solicitar el nombre del archivo de texto
        # Verificar si el archivo tiene la extensión .txt; si no, agregarla
        archivo = ruta + input("Ingrese el nombre del archivo de texto: ")
        if not archivo.endswith('.txt'):
            archivo += '.txt'
        
        # Submenú de opciones
        print("1. Contar palabras y caracteres\n2. Reemplazar palabras\n3. Histograma de vocales")
        sub_menu = int(input("Escoja la opción que quiere (1, 2, 3): "))
        print('\n' + '-'*40)

        match sub_menu:
            case 1: # Contar palabras y caracteres
                # Llamar la función para contar palabras y caracteres
                num_palabras, num_caracteres, num_caracteres_sin_espacios = txt.contar_palabras_caracteres(archivo) 
                # Imprimir los resultados
                print(f"El archivo tiene {num_palabras} palabras.")
                print(f"Caracteres (con espacios): {num_caracteres}")
                print(f"Caracteres (sin espacios): {num_caracteres_sin_espacios}")

            case 2: # Reemplazar palabras
                # Solicitar la palabra a reemplazar y la nueva palabra
                palabra_ant = input("Ingrese la palabra a reemplazar: ")
                palabra_nueva = input("Ingrese la nueva palabra: ")
                # Llamar la función para reemplazar palabras e imprimir el resultado
                txt.reemplazar_palabras(archivo, palabra_ant, palabra_nueva)
                print(f"Se ha reemplazado '{palabra_ant}' por '{palabra_nueva}' en el archivo.")

            case 3: # Histograma de vocales
                # Llamar la función para graficar el histograma de vocales
                txt.histograma_vocales(archivo)

            case _: # Ninguna de las anteriores
                print("Opción no válida. Por favor, elija una opción válida.") # Mensaje de error

    case 'C': # Procesar archivo CSV
        print("\n")
        print('-'*40)
        print("Submenú de archivos separados por comas")
        print('-'*40)

        # Solicitar el nombre del archivo CSV
        # Verificar si el archivo tiene la extensión .csv; si no, agregarla
        archivo = ruta + input("Ingrese el nombre del archivo CSV (con extensión .csv): ")
        if not archivo.endswith('.csv'):
            archivo += '.csv'

        print("1. Mostrar las 15 primeras filas\n2. Calcular estadísticas de una columna\n3. Graficar una columna")
        sub_menu = int(input("Escoja la opción que quiere (1, 2, 3): "))
        print('\n' + '-'*40)

        match sub_menu:
            case 1: # Mostrar las 15 primeras filas
                # Llamar la función para mostrar las primeras filas
                csvf.mostrar_primeras_filas(archivo)

            case 2: # Calcular estadísticas de una columna
                # Solicitar el número de la columna y llamar la función para calcular estadísticas
                columna = int(input("Ingrese el número de la columna: ")) - 1
                csvf.calcular_estadisticas(archivo, columna)

            case 3: # Graficar una columna
                # Solicitar el número de la columna y llamar la función para graficar
                columna = int(input("Ingrese el número de la columna: ")) - 1
                csvf.graficar_columna(archivo, columna)

            case _: # Ninguna de las anteriores
                print("Opción no válida. Por favor, elija una opción válida.") # Mensaje de error

    case 'S': # Salir
        print("Saliendo del programa...")

    case _: # Ninguna de las anteriores
        print("Opción no válida. Por favor, elija una opción válida.")
        print("Saliendo del programa...")
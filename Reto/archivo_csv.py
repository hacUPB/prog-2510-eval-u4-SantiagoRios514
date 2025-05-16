import csv                          # Trabajar con archivos CSV
import matplotlib.pyplot as plt     # Graficar datos

def mostrar_primeras_filas(archivo):
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_csv:
        lector = csv.reader(a_csv) # Leer el archivo CSV
        cont = 0
        # Imprimir las primeras 15 filas
        for fila in lector:
            if cont < 15:
                print(fila)
                cont += 1
            else:
                break

def calcular_estadisticas(archivo, columna):
    # Iniciar lista vacía para almacenar los datos
    datos = []

    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_csv:
        lector = csv.reader(a_csv)
        next(lector) # Saltar la primera fila (títulos)
        # Separar los datos de la columna especificada
        for fila in lector:
            valor = float(fila[columna]) # Convertir el valor a float para poder calcular estadísticas
            datos.append(valor) # Agregar el valor a la lista de datos

    datos.sort() # Ordenar los datos
    
    # Calcular estadísticas
    n = len(datos) # Número de datos
    media = sum(datos) / n
    # Mediana
    if n % 2 == 0:
        mediana = (datos[n // 2 - 1] + datos[n // 2]) / 2
    else:
        mediana = datos[n // 2]

    maximo = max(datos)
    minimo = min(datos)
    
    # Imprimir estadísticas
    print(f"Media: {media}")
    print(f"Mediana: {mediana}")
    print(f"Máximo: {maximo}")
    print(f"Mínimo: {minimo}")

def graficar_columna(archivo, columna):
    # Iniciar lista vacía para almacenar los datos
    datos = []
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_csv:
        lector = csv.reader(a_csv)
        next(lector)
        # Separar los datos de la columna especificada
        for fila in lector:
            valor = float(fila[columna])
            datos.append(valor)

    plt.plot(datos)
    plt.xlabel('Índice')
    plt.ylabel('Valor')
    plt.title('Gráfica de la columna')
    plt.show()
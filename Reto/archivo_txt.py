import matplotlib.pyplot as plt     # Graficar datos


def contar_palabras_caracteres(archivo): 
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_txt:
        contenido = a_txt.read() # Leer el contenido del archivo

        num_palabras = len(contenido.split()) # Cuenta las palabras separadas por espacios
        num_caracteres_c_esp = len(contenido) # Contar caracteres con espacios

        # Eliminar espacios y saltos de línea
        contenido = contenido.replace('\n', '')
        contenido = contenido.replace(' ', '') 
        num_caracteres_s_esp = len(contenido) # Contar caracteres sin espacios ni saltos de línea

    return num_palabras, num_caracteres_c_esp, num_caracteres_s_esp


def reemplazar_palabras(archivo, palabra_ant, palabra_nueva):
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_txt:
        contenido = a_txt.read()
    
    # Reemplazar la palabra antigua por la nueva
    palabras = contenido.split() # Separar el contenido en palabras
    for i in range(len(palabras)):
        if palabras[i] == palabra_ant:
            palabras[i] = palabra_nueva # Reemplazar la palabra antigua por la nueva
    contenido = " ".join(palabras) # Unir las palabras nuevamente en una cadena
    
    # Escribir el contenido modificado en el archivo
    with open(archivo, 'w') as a_txt_w:
        a_txt_w.write(contenido)

def histograma_vocales(archivo):
    # Abrir el archivo en modo lectura
    with open(archivo, 'r') as a_txt:
        contenido = a_txt.read().lower() # Leer el contenido del archivo y convertirlo a minúsculas
    
    # Contar las vocales
    vocales = 'aeiou'
    conteo_vocales = {}
    # Cuenta cuántas veces aparece cada vocal
    for v in vocales:
        conteo_vocales[v] = contenido.count(v) # Contar cada vocal y agregarla al diccionario
    
    # Graficar el histograma
    plt.bar(conteo_vocales.keys(), conteo_vocales.values())
    plt.xlabel('Vocales')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Vocales')
    plt.show()
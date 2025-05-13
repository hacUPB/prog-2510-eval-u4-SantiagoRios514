import os           # Listar archivos
import csv          # Archivos csv
import matplotlib   # Gráficos

print('-'*25)
print("Análisis de datos en .CSV y .TXT")
print('-'*25)

print("L. Listar archivos en la ruta actual\nT. Procesar archivo de texto (.txt)\nC. Procesar archivo separado por comas (.csv)\nS. Salir")
menu = input("Escoja la opción que quiere (L, T, C, S): ").upper()
match menu:
    case 'L':
    case 'T':

    case 'C':
    case 'S':
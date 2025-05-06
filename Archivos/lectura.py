p_archivo_datos = open("Archivos\\texto2.txt","r")
archivo_imc = open("Archivos\\imc.txt","a")
for i in range(3):
    peso = int(p_archivo_datos.readline())
    estatura = float(p_archivo_datos.readline())
    imc = peso/estatura**2
    imc = str(imc)
    archivo_imc.write(imc+"\n")

p_archivo_datos.close()
archivo_imc.close()
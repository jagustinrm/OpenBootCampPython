
archivo = open("archivo.txt", "w")
archivo.write("Primera escritura")
archivo.close()


archivo_lectura = open("archivo.txt", "r")
contenido = archivo_lectura.read()
print("Contenido del archivo:", contenido)
archivo_lectura.close()

archivo_escritura = open("archivo.txt", "w")
archivo_escritura.write("Segunda escritura")
archivo_escritura.close()
archivo_lectura = open("archivo.txt", "r")
contenido_actualizado = archivo_lectura.read()
print("Contenido actualizado del archivo:", contenido_actualizado)
archivo_lectura.close()

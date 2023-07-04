from io import open

archivo = open("archivo_prueba.txt","a")

segundomensaje=("\nEste es un mensaje que introduje con append")
archivo.write(segundomensaje)
archivo.close()


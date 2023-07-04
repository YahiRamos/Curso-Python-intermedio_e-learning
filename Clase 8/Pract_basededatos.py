import sqlite3 #Importamos la libreria de sqlite

conecta=sqlite3.connect("basedeprueba")#Abrimos una conexión
cur=conecta.cursor()#Creamos el puntero
cur.execute("DELETE FROM Alumnos")#Utilizamos Delete para eliminar la información, 
#si quieres eliminar algo especifico agregar un WHERE en el que indiques el registro que vas a borrar, 
#ya que el Delete tal como lo puse borrara todos los registros

conecta.commit()
conecta.close()#Cerramos la conección
class Vehiculos():
	
	def __init__(self, marca,modelo):
		
		self.marca= marca
		self.modelo= modelo
		self.enmarcha= False
		self.acelera=False
		self.frena= False

	def arrancar(self):
		
		self.enmarcha=True

	def acelerar(self):

		self.acelera=True

	def frenar(self):
		
		self.frena=True

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nArrancar: ",
			self.enmarcha,"\nAcelerar: ",self.acelera,"\nFrenar: ",self.frena)

class avion(Vehiculos):
	Volando=""
	def vuela(self):
		self.Volando="Puede volar" 

	def estado(self):
		print("Marca: ",self.marca,"\nModelo: ",self.modelo,"\nArrancar: ",
			self.enmarcha,"\nAcelerar: ",self.acelera,"\nFrenar: ",self.frena,"\nExtra: ",self.Volando)
				
avi=avion("Boing","747")
avi.vuela()
avi.estado()			

				
		
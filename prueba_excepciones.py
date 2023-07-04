def suma(num1, num2):
	return num1+num2

def resta(num1, num2):
	return num1-num2

def multiplica(num1, num2):
	return num1*num2

def divide(num1,num2):		
	return num1/num2

while True:
	try:
		n1=(int(input("Introduce el primer número: ")))

		n2=(int(input("Introduce el segundo número: ")))	
		break
	except ValueError:
		print("Introduzca solo numeros, intente de nuevo")
		
	
operacion=input("Introduce la operación a realizar (suma,resta,multiplica,divide): ")

if operacion=="suma":
	print(suma(n1,n2))

elif operacion=="resta":
	print(resta(n1,n2))

elif operacion=="multiplica":
	print(multiplica(n1,n2))

elif operacion=="divide":
	print(divide(n1,n2))

else:
	print ("Operación invalida")


print("Operación ejecutada. ")
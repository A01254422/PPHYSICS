#actividad1 pavel y victoria
import random

#variable para seleccionar un numero random
nr=random.randint(1, 10)

p= 0
j=input("Quieres jugar un juego? ")

while j=="si":
	if p<= 10 :
		print("He seleccionado un numero random del 1 al 10")
		nd= int(input("intenta adivinarlo... "))
		if nd>nr :
			p-=1
			print("Es mas chiquito que ese, intenta de nuevo \n Tienes ",p,"punto")
		elif  nd<nr:
			p-=1
			print("Es mas grande, intenta de nuevo \n Tienes",p," puntos")
		else:
			p+=2
			print( "LE ATINASTE \n Tienes",p," puntos")
			nr=random.randint(1, 10)
	else:
		print("HAS GANADO")
		j=input("Quieres jugar otra vez?")
		break
	

 
 

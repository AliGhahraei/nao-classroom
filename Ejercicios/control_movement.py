from finch import Finch
from time import sleep

finch = Finch()

def get_color(color):
	switcher = {'azul': '#0000FF', 'amarillo': '#FFFF00', 'verde': '#008000'}
	return switcher.get(color)

# Escribe tu codigo aqui abajo (rueda_izquierda = 0.5, rueda_derecha = 0, tiempo = 5)
rueda_izquierda = 0.5
rueda_derecha = 0
tiempo = 12
# Ahora pide al usuario que ingrese las velocidades
#rueda_izquierda = raw_input("Velocidad izquierda: ")
#rueda_derecha = raw_input("Velocidad derecha: ")

finch.wheels(rueda_izquierda, rueda_derecha)

sleep(tiempo)

print 'Bien hecho'


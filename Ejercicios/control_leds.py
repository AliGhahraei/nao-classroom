from finch import Finch
from time import sleep

finch = Finch()

def get_color(color):
	switcher = {'azul': '#0000FF', 'amarillo': '#FFFF00', 'verde': '#008000'}
	return switcher.get(color)

# Escribe tu codigo aqui abajo (color = 'azul', tiempo = 5)
color = 
tiempo = 

# Ahora pide al usuario que ingrese un color
#color = raw_input("Dame un color: ")

finch.led(get_color(color))

sleep(tiempo)

print 'Bien hecho'


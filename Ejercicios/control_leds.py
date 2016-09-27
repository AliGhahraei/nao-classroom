from finch import Finch

finch = Finch()

def get_color(color):
	switcher = {'azul': '#0000FF', 'amarillo': '#FFFF00', 'verde': '#008000'}
	return switcher.get(color)


# Escribe tu codigo aqui abajo (color = 'azul', color = 'amarillo' o color = 'verde')
color = 'azul'

# Ahora pide al usuario que ingrese un color
#color = raw_input("Dame un color: ")

finch.led(get_color(color))

print 'Bien hecho'


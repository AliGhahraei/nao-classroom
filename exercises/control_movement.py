from exercises.finch.finch import Finch
from time import sleep

finch = Finch()



###############################################################################

# Escribe tu codigo aqui abajo (rueda_izquierda = 0.5, rueda_derecha = 0, tiempo = 5)
rueda_izquierda = 
rueda_derecha = 
tiempo = 

###############################################################################

# Ahora pide al usuario que ingrese las velocidades
#rueda_izquierda = raw_input("Velocidad izquierda: ")
#rueda_derecha = raw_input("Velocidad derecha: ")

finch.wheels(rueda_izquierda, rueda_derecha)
sleep(tiempo)
finch.wheels(0, 0)

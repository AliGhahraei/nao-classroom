from finch.finch import Finch
from time import sleep

finch = Finch()
switcher = {'blue': '#0000FF', 'yellow': '#FFFF00', 'green': '#008000'}

###############################################################################

# Write your code here. Your code asks the user for a color (blue, yellow or green)

# CODE: raw_input('color:')
color = raw_input('color:')

###############################################################################

colorIsValid = False


finchColor = switcher.get(color)

while(finchColor is None):
	print('Invalid color. Valid colors are: ' + ', '.join(switcher.keys()))
	finchColor = switcher.get(raw_input('color:'))
	
	
finch.led(finchColor)

sleep(5)

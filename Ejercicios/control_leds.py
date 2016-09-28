from finch import Finch
from retry import retryColorInput

finch = Finch()
switcher = {'blue': '#0000FF', 'yellow': '#FFFF00', 'green': '#008000'}


###############################################################################

# Write your code here. Your code asks the user for a color (blue, yellow or green)
color =

###############################################################################

colorIsValid = False


finchColor = switcher.get(color)

while(finchColor is None):
	print('Invalid color. Valid colors are: ' + ', '.join(switcher.keys()))
	finchColor = switcher.get(retryColorInput())
	
	
finch.led(finchColor)
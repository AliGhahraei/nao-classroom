#!/usr/bin/python

import sys 
def parser( fileToParse, lineToParse, stringToParse):
	stringToParse = stringToParse.lower()
	stringToParse = stringToParse.replace(' ','')
	stringToParse = stringToParse.replace('\n', '')
	f = open(fileToParse)
	txt = f.readlines()
	x = txt[lineToParse]
	x = x.lower()
	x = x.replace('\n', '')
	x = x.replace(' ','')
	print x
	print stringToParse
	if x == stringToParse:
		return True
	else:
		return False


arch = "archivo.txt"
Y = parser( arch, 0, "daniel ramiro leyva leal ")
print Y

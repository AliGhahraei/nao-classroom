#!/usr/bin/python

import sys

def parser( fileToParse, lineToParse, stringToParse):
	stringToParse = stringToParse.replace(' ','')
	stringToParse = stringToParse.replace('\n', '')
	f = open(fileToParse)
	txt = f.readlines()
	x = txt[lineToParse]
	x = x.replace('\n', '')
	x = x.replace(' ','')
	print x
	print stringToParse
	if x == stringToParse:
		return True
	else:
		return False

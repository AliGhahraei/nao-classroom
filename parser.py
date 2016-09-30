#!/usr/bin/python

def parse(fileToParse, linesToParse, stringsToParse):
	fileText = open(fileToParse).readlines()
	
	for lineToParse, stringToParse in zip(linesToParse, stringsToParse):
		stringToParse = stringToParse.replace(' ','')
		stringToParse = stringToParse.replace('\n', '')
		
		stringParsed = fileText[lineToParse-1]
		stringParsed = stringParsed.replace('\n', '')
		stringParsed = stringParsed.replace(' ','')
		
		if(stringParsed != stringToParse):
			return lineToParse
		
	return None

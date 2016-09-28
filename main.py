# -*- coding: utf-8 -*-
from naoqi import *
from FileMonitor import FileMonitor

import time

from Callback import Callback


NAO_IP = "10.15.89.247"
PC_IP = '10.17.13.30'
PORT = 9559


def main():    
    tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
#    tts.say("Welcome to your first programming class with robots")
    
    nextExercise = getNextExercise()
    
    while(next != 'Zero'):
        if nextExercise == 'One':
            monitor = FileMonitor(
                tts,
                'Ejercicios/control_leds.py', 
                [11], 
                ["color = 'azul'"])
            monitor.monitor_file()
        elif nextExercise == 'Two':
            monitor.setData(
                'Ejercicios/control_movement.py', 
                [11, 12, 13], 
                ["rueda_izquierda = 0.5", "rueda_derecha = 0", "tiempo = 5"])
            monitor.monitor_file()
            
        nextExercise = getNextExercise()


def getNextExercise():
    moduleName = "Callback"
    memValue = "PictureDetected"
    
    ALBroker("pythonBroker", PC_IP,9999, NAO_IP,PORT)
    pythonModule = Callback()
    
    # Create a proxy to ALMemory
    try:
        memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
    except RuntimeError, e:
        print "Error when creating ALMemory proxy:", e
        exit(1)
    
    
    # Have the python module called back when picture recognition results change.
    try:
        memoryProxy.subscribeToEvent(memValue, moduleName, "pictureChanged")
    except RuntimeError,e:
        print "Error when subscribing to micro event"
        exit(1)
    
    
    # Let the picture recognition run for a little while (will stop after 'count' calls of the callback).
    # You can check the results using a browser connected on your Nao, then
    # Advanced -> Memory -> type PictureDetected in the field
    while pythonModule.nextExercise is not None:
        time.sleep(1)
    
    # unsubscribe modules
    memoryProxy.unsubscribeToEvent(memValue, moduleName)
    #recoProxy.unsubscribe(moduleName)
    
    return pythonModule.nextExercise

    
if  __name__ == "__main__":
    main()
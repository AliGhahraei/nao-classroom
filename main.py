# -*- coding: utf-8 -*-
from naoqi import *
from FileMonitor import FileMonitor

import time

import Callback


NAO_IP = "10.15.89.247"
PC_IP = '10.17.13.30'
PORT = 9559


def main():    
    tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
    tts.say("Welcome")
    
    nextExercise = ''
    monitor = FileMonitor(tts)
    
    while(nextExercise != 'Zero'):
        nextExercise = getNextExercise()
        
        tts.say('You selected exercise number '+nextExercise)
        if nextExercise == 'One':
            monitor.setData(
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
        elif nextExercise == 'Zero':
            tts.say('Goodbye!')
        else:
            tts.say('That number is not assigned to any lesson')


def getNextExercise():
    Callback.nextExercise = None
    
    moduleName = "Callback"
    memValue = "PictureDetected"
    
    recoProxy = ALBroker("pythonBroker", PC_IP,0, NAO_IP,PORT)
    pythonModule = Callback.Callback(moduleName)
    
    # Create a proxy to ALMemory
    try:
        memoryProxy = ALProxy("ALMemory", NAO_IP, PORT)
    except RuntimeError, e:
        print "Error when creating ALMemory proxy:", e
        exit(1)
    
    
    # Have the python module called back when picture recognition results change.
    try:
        memoryProxy.subscribeToEvent(memValue, moduleName, "pictureChanged")
    except RuntimeError, e:
        print "Error when subscribing to micro event"
        exit(1)
    
    
    # Let the picture recognition run for a little while (will stop after 'count' calls of the callback).
    # You can check the results using a browser connected on your Nao, then
    # Advanced -> Memory -> type PictureDetected in the field
    while Callback.nextExercise is None:
        time.sleep(1)
    
    # unsubscribe modules
    memoryProxy.unsubscribeToEvent(memValue, moduleName)
    
    return Callback.nextExercise

    
if  __name__ == "__main__":
    main()
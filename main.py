# -*- coding: utf-8 -*-
from naoqi import ALProxy
from FileMonitor import FileMonitor


def main():
    tts = ALProxy("ALTextToSpeech", "10.15.89.247", 9559)
    tts.say("Welcome to your first programming class with robots")
    
    monitor = FileMonitor(
        tts,
        'Ejercicios/control_leds.py', 
        [11], 
        ["color = 'azul'"])
    monitor.monitor_file()
    
    monitor.setData(
        'Ejercicios/control_movement.py', 
        [11, 12, 13], 
        ["rueda_izquierda = 0.5", "rueda_derecha = 0", "tiempo = 5"])
    monitor.monitor_file()
    
if __name__ == "__main__":
    main()
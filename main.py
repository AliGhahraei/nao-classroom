# -*- coding: utf-8 -*-
from naoqi import ALProxy
from FileMonitor import FileMonitor


def main():
    tts = ALProxy("ALTextToSpeech", "10.15.89.247", 9559)
    tts.say("Welcome to your first programming class with robots")
    
    monitor = FileMonitor('archivo.txt')
    monitor.monitor_file()
    
if __name__ == "__main__":
    main()
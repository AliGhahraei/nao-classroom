import sys
import time

IPC = "10.15.89.247"
PORT = 9559

try:
    print "try"
    motionC = ALProxy("ALMotion", IPC, PORT)
    
except Exception,e:
    print "Error when creating STMOBJECT_NAME proxy:"
    print str(e)
    exit(1)
    

from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.15.89.247", 9559)
tts.say("Hello, world!")

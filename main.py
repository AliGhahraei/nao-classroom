# -*- coding: utf-8 -*-
from naoqi.naoqi import ALProxy
from naoqi.naoqi import ALModule
from naoqi.naoqi import ALBroker
from FileMonitor import FileMonitor
from speech import introduction
from say import say
from movement.left_arm import move_left
from movement.right_arm import move_right


import time

import Callback


#NAO_IP = "10.15.85.106"
NAO_IP = '10.15.89.247'
PC_IP = '10.15.92.237'
PORT = 9559


def main():    
    tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
    stand(NAO_IP)
    time.sleep(10)
    move_left(NAO_IP, PORT)
    move_right(NAO_IP, PORT)
    # introduction()
    sit(NAO_IP)
    
    nextExercise = ''
    monitor = FileMonitor()
    
    while(nextExercise != 'Zero'):
        nextExercise = getNextExercise()
        
        say('You selected exercise number '+nextExercise,tts)
        if nextExercise == 'One':
           # say('An input is the information that is inserted into a program by an user. This information can take many forms: it can be something simple like text that was typed on the keyboard or it can be something more complex, like the image I just read a while ago.',tts)
           # say('The input is used and manipulated by the computer in order to do different things, like making a calculation, accelerate a car, or even make a videogame character attack. These all would be  outputs, which can be defined as the information provided by a computer or program.',tts)
           # say('You have to complete code for the following exercise. Follow the instructions in the comments',tts)
            monitor.setData(
                'exercises/control_leds.py', 
                [20],
                ["color = raw_input('color:')"])
            monitor.monitor_file(tts)
        elif nextExercise == 'Two':
            monitor.setData(
                'exercises/control_movement.py', 
                [20, 21, 22],
                ["rueda_izquierda = 0.5", "rueda_derecha = 0", "tiempo = 5"])
            monitor.monitor_file(tts)
        elif nextExercise == 'Zero':
            say('Goodbye!',tts)
        else:
            say('That number is not assigned to any lesson',tts)


def getNextExercise():
    Callback.nextExercise = None
    
    moduleName = "Callback"
    memValue = "PictureDetected"
    
    recoProxy = ALBroker("pythonBroker", PC_IP, 0, NAO_IP,PORT)
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

def StiffnessOn(proxy):
    #We use the "Body" name to signify the collection of all joints
    pNames = "Body"
    pStiffnessLists = 1.0
    pTimeLists = 1.0
    proxy.stiffnessInterpolation(pNames, pStiffnessLists, pTimeLists)


def stand(robotIP):
    """ Example showing a path of two positions
    Warning: Needs a PoseInit before executing
    """

    # Init proxies.
    motionProxy = ALProxy("ALMotion", robotIP, 9559)

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)


    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)

    # Send NAO to Pose Init
    postureProxy.post.goToPosture("StandInit", 0.5)
    
def sit(robotIP):
    # Init proxies.
    try:
        motionProxy = ALProxy("ALMotion", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALMotion"
        print "Error was: ", e

    try:
        postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
    except Exception, e:
        print "Could not create proxy to ALRobotPosture"
        print "Error was: ", e

    # Set NAO in Stiffness On
    StiffnessOn(motionProxy)

    postureProxy.goToPosture("Sit", 0.5)

    
if  __name__ == "__main__":
    main()

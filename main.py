import sys
import time
from naoqi import ALProxy

def preloadBehaviors ():
    beManagerC.preloadBehavior(up);
    beManagerC.preloadBehavior(tai);
    beManagerC.preloadBehavior(down);

def main():
    IPC = "10.15.89.247"
    PORT = 9559
      
    try:
        print "try"
        motionC = ALProxy("ALMotion", IPC, PORT)
        beManagerC = ALProxy("ALBehaviorManager",IPC,PORT)
        audioC = ALProxy("ALAudioDevice",IPC,PORT)
        memoryC = ALProxy("ALMemory",IPC,PORT)
        speechC = ALProxy("ALTextToSpeech",IPC,PORT)
        
    except Exception,e:
        print "Error when creating STMOBJECT_NAME proxy:"
        print str(e)
        exit(1)
        
    up = "standup"; ##Rutina para pararse
    down = "sitdown"; ##Rutina para sentarse
    tai = "taiChi"; ##Rutina de baile del taichi
    
    preloadBehaviors()
    
    beManagerC.runBehavior(up);
    #sleep de 0.5 seg para que tenga pausas entre acciones
    time.sleep(0.5);
    speechC.say( "Hello!" );
    speechC.say( "My name is Sheldon!" );
    
    motionC.post.setStiffnesses ("Body", 1.0); ##Activa los motores
    time.sleep(2);
    beManagerC.runBehavior(up);
    motionC.walkTo(0.5,0.0,0.0);
    
    speechC.say( "This is my new dance!" );
    beManagerC.runBehavior(tai);
    time.sleep(1.5);
    
    speechC.post.say( "I am tired, I'm going to sit" );
    beManagerC.runBehavior(down);
    motionC.setStiffnesses( "Body" ,0.0);
    exit(0);

import sys
import motion
import time
from naoqi import ALProxy

def preloadBehaviors ():
    beManagerC.preloadBehavior(up);
    beManagerC.preloadBehavior(tai);
    beManagerC.preloadBehavior(down);


IPC = "10.15.89.247";
PORT = 9559;
  
try:
    print "try"
    motionC = ALProxy("ALMotion", IPC, PORT)
    beManagerC = ALProxy("ALBehaviorManager",IPC,PORT)
    audioC = ALProxy("ALAudioDevice",IPC,PORT)
    memoryC = ALProxy("ALMemory",IPC,PORT)
    speechC = ALProxy("ALTextToSpeech",IPC,PORT)
    postureProxy = ALProxy("ALRobotPosture", IPC, PORT)
    
except Exception,e:
    print "Error when creating STMOBJECT_NAME proxy:"
    print str(e)
    exit(1)
    
# postureProxy.goToPosture("StandInit", 1.0)
# postureProxy.goToPosture("SitRelax", 1.0)
# postureProxy.goToPosture("StandZero", 1.0)
# postureProxy.goToPosture("LyingBelly", 1.0)
# postureProxy.goToPosture("LyingBack", 1.0)
# postureProxy.goToPosture("Stand", 1.0)
# postureProxy.goToPosture("Crouch", 1.0)
# postureProxy.goToPosture("Sit", 1.0)

up = "standup"; ##Rutina para pararse
down = "sitdown"; ##Rutina para sentarse
tai = "taiChi"; ##Rutina de baile del taichi

#preloadBehaviors()

id = beManagerC.post.runBehavior(up);
#sleep de 0.5 seg para que tenga pausas entre acciones
speechC.say( "Hello!" );
speechC.say( "I can speak while i am moving. I am invinsible" );
motion.wait(id)

# motionC.post.setStiffnesses ("Body", 1.0); ##Activa los motores
# time.sleep(2);
# beManagerC.runBehavior(up);
# time.sleep(2);
# motionC.walkTo(0.5,0.0,0.0);

# speechC.say( "This is my new dance!" );
# beManagerC.runBehavior(tai);
# time.sleep(1.5);

JointNames = ["LShoulderPitch", "LShoulderRoll", "LElbowYaw", "LElbowRoll"]
Arm1 = [-40,  25, 0, -40]
Arm1 = [ x * motion.TO_RAD for x in Arm1]

Arm2 = [-40,  50, 0, -80]
Arm2 = [ x * motion.TO_RAD for x in Arm2]

pFractionMaxSpeed = 0.6

speechC.post.say( "I will stretch my arms" )
motionC.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)
motionC.angleInterpolationWithSpeed(JointNames, Arm2, pFractionMaxSpeed)
motionC.angleInterpolationWithSpeed(JointNames, Arm1, pFractionMaxSpeed)

exit(0);

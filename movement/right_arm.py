# Choregraphe simplified export in Python.
from naoqi import *

NAO_IP = "10.15.89.247"
PC_IP = '10.15.87.188'
PORT = 9559

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.20000])
keys.append([ -0.05373])

names.append("HeadYaw")
times.append([ 0.20000])
keys.append([ -0.03686])

names.append("LAnklePitch")
times.append([ 0.20000])
keys.append([ 0.85133])

names.append("LAnkleRoll")
times.append([ 0.20000])
keys.append([ -0.01070])

names.append("LElbowRoll")
times.append([ 0.20000, 0.80000, 1.60000])
keys.append([ -1.21182, -0.62483, -1.33867])

names.append("LElbowYaw")
times.append([ 0.20000])
keys.append([ -0.43723])

names.append("LHand")
times.append([ 0.20000, 0.40000, 0.80000, 1.60000])
keys.append([ 0.00516, 0.00733, 0.01257, 0.00419])

names.append("LHipPitch")
times.append([ 0.20000])
keys.append([ -1.53396])

names.append("LHipRoll")
times.append([ 0.20000])
keys.append([ 0.27309])

names.append("LHipYawPitch")
times.append([ 0.20000])
keys.append([ -0.57981])

names.append("LKneePitch")
times.append([ 0.20000])
keys.append([ 1.39897])

names.append("LShoulderPitch")
times.append([ 0.20000, 0.40000, 0.80000, 1.60000])
keys.append([ 0.91576, 0.52185, -0.14486, 1.18682])

names.append("LShoulderRoll")
times.append([ 0.20000, 0.80000, 1.60000])
keys.append([ 0.24233, 0.89361, 0.31241])

names.append("LWristYaw")
times.append([ 0.20000, 0.80000, 1.60000])
keys.append([ 0.02757, -1.82387, -1.49226])

names.append("RAnklePitch")
times.append([ 0.20000])
keys.append([ 0.84834])

names.append("RAnkleRoll")
times.append([ 0.20000])
keys.append([ 0.01231])

names.append("RElbowRoll")
times.append([ 0.20000])
keys.append([ 1.25025])

names.append("RElbowYaw")
times.append([ 0.20000])
keys.append([ 0.50925])

names.append("RHand")
times.append([ 0.20000])
keys.append([ 0.00525])

names.append("RHipPitch")
times.append([ 0.20000])
keys.append([ -1.52330])

names.append("RHipRoll")
times.append([ 0.20000])
keys.append([ -0.26381])

names.append("RHipYawPitch")
times.append([ 0.20000])
keys.append([ -0.57981])

names.append("RKneePitch")
times.append([ 0.20000])
keys.append([ 1.40979])

names.append("RShoulderPitch")
times.append([ 0.20000])
keys.append([ 0.93578])

names.append("RShoulderRoll")
times.append([ 0.20000])
keys.append([ -0.29150])

names.append("RWristYaw")
times.append([ 0.20000])
keys.append([ -0.02152])

try:
    #uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = ALProxy("ALMotion", NAO_IP, 9559)
    motion.angleInterpolation(names, keys, times, True);
except BaseException, err:
    print err


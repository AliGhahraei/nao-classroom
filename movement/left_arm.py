# -*- coding: utf-8 -*-
from naoqi import *
from FileMonitor import FileMonitor
from speech import introduction

import time

import Callback


NAO_IP = "10.15.89.247"
PC_IP = '10.15.87.188'
PORT = 9559

# Choregraphe simplified export in Python.

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.50000])
keys.append([ -0.05373])

names.append("HeadYaw")
times.append([ 0.50000])
keys.append([ -0.03379])

names.append("LAnklePitch")
times.append([ 0.50000])
keys.append([ 0.85133])

names.append("LAnkleRoll")
times.append([ 0.50000])
keys.append([ -0.01070])

names.append("LElbowRoll")
times.append([ 0.50000])
keys.append([ -1.31766])

names.append("LElbowYaw")
times.append([ 0.50000])
keys.append([ -0.52160])

names.append("LHand")
times.append([ 0.50000])
keys.append([ 0.00443])

names.append("LHipPitch")
times.append([ 0.50000])
keys.append([ -1.53396])

names.append("LHipRoll")
times.append([ 0.50000])
keys.append([ 0.27309])

names.append("LHipYawPitch")
times.append([ 0.50000])
keys.append([ -0.57981])

names.append("LKneePitch")
times.append([ 0.50000])
keys.append([ 1.39897])

names.append("LShoulderPitch")
times.append([ 0.50000])
keys.append([ 1.00933])

names.append("LShoulderRoll")
times.append([ 0.50000])
keys.append([ 0.39266])

names.append("LWristYaw")
times.append([ 0.50000])
keys.append([ -1.52944])

names.append("RAnklePitch")
times.append([ 0.50000])
keys.append([ 0.84988])

names.append("RAnkleRoll")
times.append([ 0.50000])
keys.append([ 0.01231])

names.append("RElbowRoll")
times.append([ 0.50000, 1.00000])
keys.append([ 1.24258, 0.65275])

names.append("RElbowYaw")
times.append([ 0.50000])
keys.append([ 0.51692])

names.append("RHand")
times.append([ 0.50000])
keys.append([ 0.00525])

names.append("RHipPitch")
times.append([ 0.50000])
keys.append([ -1.52330])

names.append("RHipRoll")
times.append([ 0.50000])
keys.append([ -0.26381])

names.append("RHipYawPitch")
times.append([ 0.50000])
keys.append([ -0.57981])

names.append("RKneePitch")
times.append([ 0.50000])
keys.append([ 1.40979])

names.append("RShoulderPitch")
times.append([ 0.50000, 1.00000, 2.00000, 3.50000])
keys.append([ 0.94805, 0.40492, -0.31940, 0.78191])

names.append("RShoulderRoll")
times.append([ 0.50000, 2.00000, 3.50000])
keys.append([ -0.31298, -0.92328, 0.00175])

names.append("RWristYaw")
times.append([ 0.50000, 1.00000, 2.00000])
keys.append([ -0.02305, -0.76271, 1.82387])

try:
    # uncomment the following line and modify the IP if you use this script outside Choregraphe.
    motion = ALProxy("ALMotion", NAO_IP, 9559)
    motion.angleInterpolation(names, keys, times, True);
except BaseException, err:
    print err



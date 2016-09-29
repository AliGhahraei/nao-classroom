# Choregraphe simplified export in Python.
from naoqi import ALProxy
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([ 0.40000, 0.80000, 1.20000, 1.60000, 2.00000])
keys.append([ -0.03993, -0.55501, 0.25831, -0.55501, -0.03993])

names.append("HeadYaw")
times.append([ 0.40000, 0.80000, 1.20000, 1.60000, 2.00000])
keys.append([ -0.03072, -0.03072, -0.03072, -0.03072, -0.03072])

try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", IP, 9559)
  motion.angleInterpolation(names, keys, times, True);
except BaseException, err:
  print err


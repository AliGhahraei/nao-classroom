 # -*- coding: utf-8 -*-

from naoqi import ALProxy

tts = ALProxy("ALTextToSpeech", "10.15.89.247", 9559)
tts.say("la programación es una herramienta")

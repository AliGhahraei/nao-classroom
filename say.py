import time
import random
import sys

def say(text, tts):
    tts.say(text)

    typing_speed = 40

    for word in text:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    
    print ''

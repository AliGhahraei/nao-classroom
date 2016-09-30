"""Define functions related to speech.

Functions:
say -- Say a text and print it in terminal.
"""

import time
import random
import sys


def say(text, tts):
    """Make Nao say text and also print it in the terminal in a hacker fashion.

    Keyword arguments:
    text -- output text for the Nao and terminal.
    tts -- Nao proxy.
    """
    tts.say(text)

    typing_speed = 95

    for word in text:
        sys.stdout.write(word)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)

    print ''

"""Define functions related to speech.

Functions:
say -- Say a text and print it in terminal.
"""

import time
import random
import sys
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def say(text, tts):
    """Make Nao say text and also print it in the terminal in a hacker fashion.

    Keyword arguments:
    text -- output text for the Nao and terminal.
    tts -- Nao proxy.
    """
    tts.say(text)

    typing_speed = 95
    ascii_art = """
==================================================================
      ___       ___           ___           ___           ___     
     /\__\     /\  \         |\__\         /\__\         /\  \    
    /:/  /    /::\  \        |:|  |       /:/  /        /::\  \   
   /:/  /    /:/\:\  \       |:|  |      /:/  /        /:/\:\  \  
  /:/  /    /::\~\:\  \      |:|__|__   /:/__/  ___   /::\~\:\  \ 
 /:/__/    /:/\:\ \:\__\     /::::\__\  |:|  | /\__\ /:/\:\ \:\__\ 
 \:\  \    \:\~\:\ \/__/    /:/~~/~     |:|  |/:/  / \/__\:\/:/  /
  \:\  \    \:\ \:\__\     /:/  /       |:|__/:/  /       \::/  / 
   \:\  \    \:\ \/__/     \/__/         \::::/__/        /:/  /  
    \:\__\    \:\__\                      ~~~~           /:/  /   
     \/__/     \/__/                                     \/__/    

==================================================================="""

    print bcolors.BOLD+ bcolors.OKGREEN + ascii_art
    for word in text:
        sys.stdout.write(bcolors.BOLD + bcolors.OKGREEN + word)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print bcolors.ENDC + ''

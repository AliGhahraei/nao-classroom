import os
import time

from parser import parse


class FileMonitor:
    def __init__(self, tts):
        self.tts = tts
        
    def setData(self, fileName, lines, strings):
        self.FILE_NAME = fileName
        self.LINES = lines
        self.STRINGS = strings
    
    def read_stamp(self):
        return os.stat(self.FILE_NAME).st_mtime
        
    def wait_and_read(self):
        time.sleep(1)
        return self.read_stamp()
    
    def monitor_file(self):
        exercise_completed = False
        
        # time stamps tracking the modification time stamp of the file
        past_stamp = self.read_stamp()
    
        while not exercise_completed:
            new_stamp = self.wait_and_read()
            
            while new_stamp == past_stamp:
                new_stamp = self.wait_and_read()
        
            past_stamp = new_stamp
            
            parse_response = parse(self.FILE_NAME, self.LINES, self.STRINGS)
            
            if parse_response == 0:
                self.tts.say('Good job!')
                execfile(self.FILE_NAME)
                exercise_completed = True
            else:
                self.tts.say('Oops! Error on line '+str(parse_response))
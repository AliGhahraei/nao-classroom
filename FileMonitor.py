import os
import time

from parser import parse


class FileMonitor:
    def __init__(self, path):
        self.FILE_PATH = path
        
    def read_stamp(self):
        return os.stat(self.FILE_PATH).st_mtime
        
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
            if parse(self.FILE_PATH, 0, "daniel ramiro leyva leal "):
                print('bien')
                exercise_completed = True
            else:
                print('mal') 
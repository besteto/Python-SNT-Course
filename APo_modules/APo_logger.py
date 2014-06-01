import os
import datetime

class Logger:
    __colors = {}
    __colors['cyan'] = '\033[96m'
    __colors['purple'] = '\033[95m'
    __colors['blue'] = '\033[94m'
    __colors['green'] = '\033[92m'
    __colors['yellow'] = '\033[93m'
    __colors['red'] = '\033[91m'
    __colors['end'] = '\033[0m'

    def __init__(self):
        self.logFile = open(str(datetime.datetime.now())+".txt", "a")

    def info(self, msg):
        self.logFile.write(msg+"\n")
        print('green', msg)

    def destroy(self):
        self.logFile.close()
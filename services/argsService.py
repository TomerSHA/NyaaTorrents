import os
import sys
import Config

class ArgsException(Exception):
    def __init__(self, value):
        self.parameter = value
    def __str__(self):
        return repr(self.parameter)

def raiseArgsException(msg):
    raise ArgsException(msg)

def getAnimeName():
    return sys.argv[1] or raiseArgsException('not enough arguements')
def getQuality():
    return sys.argv[2] or Config.getDefaultQuality()

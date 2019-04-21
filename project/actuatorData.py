'''
Created on Apr 18, 2019
This class is created to create an Actuator Data to interact with Raspberry Pi

@author: Venkat Prasad Krishnamurthy
'''
from project.sensor_hat import Sense

class ActuatorData(object):
    '''
    classdocs
    '''

    def __init__(self):
        '''
        Constructor
        '''
        self.led        = False
        self.message    = None
        self.brightness = 0
        self.sens       = Sense()
    
    '''
    Function to switch on the heater
    '''
    def setHeater(self):
        self.led        = True
        print("Switch on Heater")
    '''
    Function to switch on the Air Cooler
    '''    
    def setCooler(self):
        self.led        = True
        print("Switch on Cooler")
        
    def resetLed(self):
        self.led        = False
        print("Switch off Cooler and Heater")    
    
    '''
    Function to adjust the brightness of light
    '''    
    def setlightBrightness(self,bright):
        self.brightness = bright
    
    '''
    Function to set message in Sensehat
    '''    
    def setMessage(self,message):
        self.message = message
        self.sens.show_message(self.message)
    
    '''
    Function to switch on the humidifier
    '''    
    def setHumid(self):
        print("Switch on humidifier")
        
    '''
    Function to switch off the heater
    '''    
    def resetHumid(self):
        print("Switch off humidifier")
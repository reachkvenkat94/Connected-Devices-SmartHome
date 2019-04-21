'''
Created on Apr 16, 2019

@author: Venkat Prasad Krishnamurthy
'''

from project.settings import Settings
from project.sensor_hat import Sense
from threading import Thread
from time import sleep

class SensorData(Thread):
    '''
    This class contains variables and methods to acquire sensor values from sensehat
    '''
    temp        = 0
    humid       = 0
    light       = 0
    sampleCount = 0
    temp_avg    = 0
    humid_avg   = 0


    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.hat           = Sense()
        self.set           = Settings()
        self.update()
        self.sampleCount   = 1
        self.temp_avg      = (self.temp_avg+self.temp)/self.sampleCount
        self.humid_avg     = (self.humid_avg+self.temp)/self.sampleCount
        self.sensors       = self.set.read()
        self.status        = self.sensors[0]
        self.temp_set      = self.sensors[1]
        self.humid_set     = self.sensors[2]
    
    '''
    This function is used to get temperature
    @return: Temperature
    '''    
    def getTemp(self):
        self.temp = self.hat.get_temperature_from_humidity()
        return self.temp
    
    '''
    This function is used to get humidity
    @return: Humidity
    '''
    def getHumid(self):
        self.humid = self.hat.get_temperature_from_humidity()
        return self.temp
    
    '''
    This function is used to get light intensity
    @return: Luminosity
    '''
    def getLight(self):
        self.light = self.hat.get_light_intensity()
        return self.light
    
    '''
    Function used to update sensor values
    '''
    def update(self):
        self.temp = self.hat.get_temperature_from_humidity()
        self.humid = self.hat.get_humidity()
        self.light = self.hat.get_light_intensity()
        self.sampleCount = self.sampleCount+1
        self.temp_avg = (self.temp_avg+self.temp)/self.sampleCount
        self.humid_avg = (self.humid_avg+self.humid)/self.sampleCount
    
    '''
    Function used to update user settings values
    '''    
    def load(self):
        set.sensors = set.read()
        self.status = self.sensors[0]
        self.temp_set = self.sensors[1]
        self.humid_set = self.sensors[2]
    
    '''
    This function is used to transform object to format used to send via HTTP
    '''    
    def generate_data(self):
        payload = {"temperature": self.temp,
               "humidity": self.humid,
               "luminosity": self.light,
               "temperature_avg":self.temp_avg,
               "humidity_avg":self.humid_avg}
        return payload
    
    '''
    This thread is used to retrieve user settings from settings.csv
    '''
    def run(self):
        while True:
            sen = self.set.read()
            if(self.status!=sen[0]|self.temp_set!=sen[1]|self.humid_set!=sen[2]):
                self.load()
                self.sampleCount = 0
                self.temp_avg = 0
                self.humid_avg = 0
                self.update()
            sleep(60)
                
            
            
            
        
        
        
        
'''
Created on Apr 19, 2019

@author: Venkat Prasad Krishnamurty
'''
from threading import Thread
from project.actuatorData import ActuatorData
from project.settings import Settings
from project.sensorData import SensorData
from labs.module06.MqttClientConnector import MqttClientConnector
from time import sleep

class ActuatorEmulator(Thread):
    '''
    This class is used to send signal to actuator every 60 seconds and
    subscribe to actuator signal from cloud
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        Thread.__init__(self)
        self.temp_topic        = "/v1.6/devices/smart_home/temp-act/lv"
        self.led               = False
        self.message           = None
        self.brightness        = 0
        self.actuator          = ActuatorData()
        self.set               = Settings()
        self.sensor            = SensorData()
        self.temp_mqtt         = MqttClientConnector(self.temp_topic)
        self.temp_mqtt.subscribe(self.temp_topic)
        
    
    '''
    This thread is used to collect values from cloud using mqtt
    Based on given conditions, will send signal to actuator through sensehat
    Thread runs once every 60 seconds
    '''    
    def run(self):
        while True:
            print("Temperature Actuator Value: "+str(self.temp_mqtt.message()))
            if self.temp_mqtt.message() == 30 or self.sensor.temp_avg<self.sensor.temp_set: 
                self.led = self.actuator.setHeater()
            elif self.sensor.temp_avg>self.sensor.temp_set or self.temp_mqtt.message() == 16:
                self.led = self.actuator.setCooler()
            else:
                None
                
            if self.sensor.humid_avg<self.sensor.humid_set: 
                self.led = self.actuator.setHumid()
            else:
                self.led = self.actuator.resetHumid()
                
            self.brightness = self.actuator.setlightBrightness(0)
            
            if self.set.status ==1:
                self.actuator.setMessage(self.message)
            
            sleep(60)
            
            

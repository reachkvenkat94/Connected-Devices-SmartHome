'''
Created on Apr 17, 2019

@author: Venkat Prasad Krishnamurthy
'''
from threading import Thread
from project.SmtpClientConnector import SmtpClientConnector
from project.MqttClientConnector import MqttClientConnector
from project.sensorData import SensorData
from project.actuatorData import ActuatorData
from time import sleep

class SensorMonitor(Thread):
    '''
    This class is used to read sensor values from Sensehat and push it to cloud
    using HTTP every 60 seconds
    '''
    CRITICAL_TEMP    = 40
    CRITICAL_HUMID   = 60
    def __init__(self):
        Thread.__init__(self)
        self.smt     = SmtpClientConnector()
        self.mqt     = MqttClientConnector("http")
        self.sensor  = SensorData()
        self.act     = ActuatorData()
        print("Sensor Monitor Object Created")
        
    
    '''
    This thread is used to retrieve sensor values, notify through smtp if the sensor values breach threshold 
    push the sensor values to cloud using http
    '''    
    def run(self):
        while True:
            self.sensor.update()
            payload = self.sensor.generate_data()
            print("Current Temperature: "+str(self.sensor.temp))
            print("Current Humidity: "+str(self.sensor.humid))
            print("Luminosity: "+str(self.sensor.light))
            self.mqt.post_request(payload)
            if self.sensor.temp > self.CRITICAL_TEMP:
                print("Critical Temp reached")
                data = ("Temperature crossed critical limit: Action Needed")
                self.smt.publishMessage("Critical Notification alert", data);
            if self.sensor.status == 0:
                if self.sensor.light>2000:
                    message = "Switch off the light"
                    self.act.setMessage(message)
                    print("Swith off the light")
                elif self.sensor.light<200:
                    message = "Switch on the light"
                    self.act.setMessage(message)
                    print("Switch on the light")
                else:
                    message = "Adjust the Brightness"
                    self.act.setMessage(message)
                    print("Adjust Brightness")
            if self.sensor.humid > self.CRITICAL_HUMID:
                print("Critical Humidity reached")
                data = ("Humidity crossed critical limit: Action Needed")
                self.smt.publishMessage("Critical Notification alert", data);
            print("Loop Completed")
            sleep(60)
                
            
            
        
        
        

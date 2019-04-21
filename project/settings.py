'''
Created on Apr 14, 2019

@author: Venkat Prasad Krishnamurthy
'''

import csv

class Settings():
    '''
    This class has functions to read user defined 
    settings from csv file
    '''
    status  = 0
    humid   = 0
    temp    = 0


    def __init__(self):
        '''
        Constructor
        '''
        self.sensors = []
        
    
    '''
    This function is used to read the user settings from settings.csv
    @return: status,temperature,humidity
    '''
    def read(self):
        try:
            f = open('settings.csv','r')
            reader = csv.reader(f)
            for row in reader:
                self.status = int(row[0])
                self.temp   = float(row[1])
                self.humid  = float(row[2])
            self.sensors.append(self.status)
            self.sensors.append(self.temp)
            self.sensors.append(self.humid)
            f.close()
        except:
            print("Error in opening file")    
        return self.sensors
        
    '''
    This function is used to update the file with latest user settings
    @param status: Status of device
    @param temp: Required Temperature
    @param humid: Required Humidity
    '''
    def write(self,status,temp,humid):
        sensors = [status,temp,humid]
        try:
            f = open('settings.csv','w')
            write = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            write.writerow(sensors)
            f.close()
        except:
            print("Error in opening file")     
        
        
        
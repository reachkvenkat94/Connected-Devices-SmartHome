'''
Created on Apr 19, 2019
This script runs the thread to
1. Measure sensor values and upload to cloud
2. Retrieve values from cloud and send signal to Actuator
3. Check for update in user settings

@author: Venkat Prasad Krishnamurthy
'''



from project.sensor_monitor import SensorMonitor
from project.actuator_emulator import ActuatorEmulator
from project.sensorData import SensorData
from time import sleep


sens_mon  = SensorMonitor()
act_emu   = ActuatorEmulator()
sensor    = SensorData()
print("Entering sensor monitor!!")
sens_mon.start()
sleep(5)
print("Entering actuator emulator!!")
act_emu.start()
print("Loading Settings!!!")
sensor.start()


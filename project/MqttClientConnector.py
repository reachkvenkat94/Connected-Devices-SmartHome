'''
Created on Feb 25, 2019
This Class is used to connect to a MQTT broker for publishing and subscription

@author: Venkat Prasad Krishnamurthy
'''

import paho.mqtt.client as mqtt    #import client library
import paho.mqtt.publish as publish
from asyncio.tasks import sleep
import time
import requests
from project.ConfigUtil import ConfigUtil
from project import ConfigConst

class MqttClientConnector():
    json_data = "Hello"
    
    
    '''
    Callback function: This function will execute once the client connects
    with MQTT Broker
    '''
    def on_connect(self,client,userdata,flags,rc):
        print("Connected with Client: "+str(rc))
        print("Connected!!!!Subscribing to topic: "+self.topic)
        client.subscribe(self.topic,0)
    
    '''
    Callback function: This function will execute once the client receives message
    from MQTT Broker
    ''' 
    def on_message(self,client,userdata,msg):
        global json_data
        json_data = str(msg.payload.decode("utf-8"))
        print(json_data)
             
    '''
    Constructor
    @param topic:topic of the message published or subscribed 
    ''' 
    def __init__(self,topic):
        self.topic        = topic;
        self.config       = ConfigUtil('../../../config/ConnectedDevicesConfig.props')
        self.host         = self.config.getProperty(ConfigConst.UBIDOTS_CLOUD_SECTION, ConfigConst.HOST_KEY)
        self.port         = self.config.getProperty(ConfigConst.UBIDOTS_CLOUD_SECTION, ConfigConst.HOST_KEY)
        self.http_host    = self.config.getProperty(ConfigConst.HTTP_CLOUD_SECTION, ConfigConst.HOST_KEY)
        self.DEVICE_LABEL = self.config.getProperty(ConfigConst.CONSTRAINED_DEVICE, ConfigConst.LABEL)
        self.url          = "{}/api/v1.6/devices/{}".format(self.http_host, self.DEVICE_LABEL)
        self.TOKEN        = self.config.getProperty(ConfigConst.UBIDOTS_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY)
        self.config.loadConfig();
   
    '''
    Function is used to publish the message
    @param topic: Topic of the message
    @param message: Message to be sent
    @param host: address of MQTT broker   
    '''
    def publish(self,topic,message,host):
        client = mqtt.Client();
        client.username_pw_set(username=self.TOKEN)
        client.connect(host,1883)
        client.publish(topic,message)
        
    '''
    Function is used to subscribe to a topic
    @param host: Address of MQTT broker 
    '''
    def subscribe(self,topic):
        self.topic = topic
        client = mqtt.Client()
        client.username_pw_set(self.TOKEN,password="")
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        print("subscribing to topic"+topic)
        client.connect(self.host,1883,60)
        print("Client Connecting......")
        client.subscribe(self.topic,0)
        client.loop_start()
        

    '''
    Function is used to store the data received from MQTT Broker
    @return: Data received from MQTT Broker
    '''
    def message(self):
        global json_data
        return json_data
    
    '''
    Function is used to Send data to cloud using POST request 
    @payload: Data to be sent to cloud
    '''
    def post_request(self,payload):
    # Creates the headers for the HTTP requests
        headers = {"X-Auth-Token": self.TOKEN, "Content-Type": "application/json"}

        # Makes the HTTP requests
        status = 400
        attempts = 0
        while status >= 400 and attempts <= 5:
            req = requests.post(url=self.url, headers=headers, json=payload)
            status = req.status_code
            attempts += 1
            time.sleep(1)

        # Processes results
        if status >= 400:
            print("[ERROR] Could not send data after 5 attempts, please check \
                your token credentials and internet connection")
            return False

        print("[INFO] request made properly, your device is updated")
        return True
        
        
        
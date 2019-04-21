'''
Created on Jan 19, 2019

@author: Venkat Prasad Krishnamurthy
'''

from project import ConfigUtil
from project import ConfigConst
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class SmtpClientConnector(object):
    '''
    classdocs
    This class contains functions to connect to mail server through smtp
    '''

    def __init__(self):
        self.config = ConfigUtil.ConfigUtil('../../../config/ConnectedDevicesConfig.props');
        self.config.loadConfig();
        
    '''
    publishMessage function is used to construct the message which is sent as notification in case of breach
    
    @param topic: Subject of Email
    @param data: Sensor notification
    '''
        
    def publishMessage(self, topic, data):
        host           = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.HOST_KEY);
        port           = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.PORT_KEY);
        fromAddr       = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.FROM_ADDRESS_KEY);
        toAddr         = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.TO_ADDRESS_KEY);
        authToken      = self.config.getProperty(ConfigConst.SMTP_CLOUD_SECTION, ConfigConst.USER_AUTH_TOKEN_KEY);
        msg            = MIMEMultipart();
        msg['From']    = fromAddr;
        msg['To']      = toAddr;
        msg['Subject'] = topic;
        msgBody        = str(data);
        msg.attach(MIMEText(msgBody));
        msgText        = msg.as_string();
        # send e-mail notification
        try:  
            # connecting to the smtp server through given port
            smtpServer = smtplib.SMTP_SSL(host, port); 
            smtpServer.ehlo();
            smtpServer.login(fromAddr, authToken); 
            smtpServer.sendmail(fromAddr, toAddr, msgText); 

        except:
            print("Error in Sending Mail");
        
        finally:
            smtpServer.close();

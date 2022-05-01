import paho.mqtt.client as mqtt
import json

class Mqtt_publisher:
    """ Class which contains functionality of an MQTT Message publisher """ 

    def __init__(self):
        """ Initialize the client with settings like: """
        self.mqttBroker = "mqtt.eclipseprojects.io"
        self.client = mqtt.Client("INTERNAL_PUBLISHER")
        self.client.connect(self.mqttBroker)
        print('[MQTT INTERNAL PUBLISHER] Client started')

    def publishDefault(self, currentTime, currentLocation, detected_flag, detectedCount, lowestConfidence, highestConfidence):
        """ Publish a default message containing no specific string Message """
        msg = json.dumps({'time' : currentTime, 
                        'location' : currentLocation,  
                        'detected' : detected_flag, 
                        'detectedCount' : detectedCount,
                        'lowestConfidence' : lowestConfidence,
                        'highestConfidence' : highestConfidence
                        }, indent = 4)

        self.client.publish("DWLS_DETECTION", msg)

    def publishMsg(self, message, currentTime, currentLocation, detected_flag, detectedCount, lowestConfidence, highestConfidence):
        """ Publish a message containing a string message at the start """
        msg = json.dumps({'msg' : message,
                        'time' : currentTime, 
                        'location' : currentLocation,  
                        'detected' : detected_flag, 
                        'detectedCount' : detectedCount,
                        'lowestConfidence' : lowestConfidence,
                        'highestConfidence' : highestConfidence
                        }, indent = 4)
        self.client.publish("DWLS_DETECTION", msg)
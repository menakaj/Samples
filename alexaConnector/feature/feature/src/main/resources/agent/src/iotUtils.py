#!/usr/bin/env python

"""
/**
* Copyright (c) 2015, WSO2 Inc. (http://www.wso2.org) All Rights Reserved.
*
* WSO2 Inc. licenses this file to you under the Apache License,
* Version 2.0 (the "License"); you may not use this file except
* in compliance with the License.
* You may obtain a copy of the License at
*
* http://www.apache.org/licenses/LICENSE-2.0
*
* Unless required by applicable law or agreed to in writing,
* software distributed under the License is distributed on an
* "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
* KIND, either express or implied. See the License for the
* specific language governing permissions and limitations
* under the License.
**/
"""

import time
import ConfigParser, os
import random
import running_mode

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#           HOST_NAME(IP) of the Device
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
global HOST_NAME
HOST_NAME = "0.0.0.0"
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
HTTP_SERVER_PORT = 5678 # http server port which is listning on

global LAST_TEMP
LAST_TEMP = 25  # The Last read temperature value from the DHT sensor. Kept globally
# Updated by the temperature reading thread
# Associate pin 23 to TRIG
TEMPERATURE_READING_INTERVAL_REAL_MODE = 3
TEMPERATURE_READING_INTERVAL_VIRTUAL_MODE = 60
TEMP_PIN = 4
TEMP_SENSOR_TYPE = 11
BULB_PIN = 11  # The GPIO Pin# in RPi to which the LED is connected
global GPIO

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#       Device specific info when pushing data to server
#       Read from a file "deviceConfig.properties" in the same folder level
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
configParser = ConfigParser.RawConfigParser()
configFilePath = os.path.join(os.path.dirname(__file__), './deviceConfig.properties')
configParser.read(configFilePath)

SERVER_NAME = configParser.get('Device-Configurations', 'server-name')
DEVICE_OWNER = configParser.get('Device-Configurations', 'owner')
DEVICE_ID = configParser.get('Device-Configurations', 'deviceId')
MQTT_EP = configParser.get('Device-Configurations', 'mqtt-ep')
# XMPP_EP = configParser.get('Device-Configurations', 'xmpp-ep')
AUTH_TOKEN = configParser.get('Device-Configurations', 'auth-token')
CONTROLLER_CONTEXT = configParser.get('Device-Configurations', 'controller-context')
# MQTT_SUB_TOPIC = configParser.get('Device-Configurations', 'mqtt-sub-topic').format(owner = DEVICE_OWNER, deviceId = DEVICE_ID)
# MQTT_PUB_TOPIC = configParser.get('Device-Configurations', 'mqtt-pub-topic').format(owner = DEVICE_OWNER, deviceId = DEVICE_ID)
DEVICE_INFO = '{{"event":{{"metaData":{{"owner":"' + DEVICE_OWNER + '","type":"raspberrypi","deviceId":"' + DEVICE_ID + '","time":{}}},"payloadData":{{"temperature":{:.2f}}}}}}}'
BRAIN_WAVE_INFO = '{{"event":{{"metaData":{{"owner":"' + DEVICE_OWNER + '","type":"raspberrypi","deviceId":"' + DEVICE_ID \
                  + '","time":{}}},"payloadData":{{"poorSignalLevel":{:.0f},"meditationLevel":{:.0f},"attentionLevel":{:.0f}, ' \
                    '"EEGPowersDelta":{:.0f},"EEGPowersTheta":{:.0f},"EEGPowersLowAlpha":{:.0f},' \
                    '"EEGPowersHighAlpha":{:.0f}, "EEGPowersLowBeta":{:.0f}, "EEGPowersHighBeta":{:.0f}, "EEGPowersLowGamma":{:.0f}, , "EEGPowersMidGamma":{:.0f}}}}}}}'
HTTPS_EP = configParser.get('Device-Configurations', 'https-ep')
# HTTP_EP = configParser.get('Device-Configurations', 'http-ep')
# APIM_EP = configParser.get('Device-Configurations', 'apim-ep')
# DEVICE_IP = '"{ip}","value":'
# DEVICE_DATA = '"{temperature}"'  # '"{temperature}:{load}:OFF"'


# {"event": {"metaData": {"owner": "admin", "type": "arduino","deviceId": "s15kdwf34vue","time": 0},"payloadData": { "temperature": 22} }}



### ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def main():
    global HOST_NAME
    # HOST_NAME = getDeviceIP()
    if running_mode.RUNNING_MODE == 'N':
        print("mode N")
        # setUpGPIOPins()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

if __name__ == '__main__':
    main()

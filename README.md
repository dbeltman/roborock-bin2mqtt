# roborock-bin2mqtt

## Simple python script to scrape last time dustbin was cycled from valetudo-enabled vacuums (tested on S50)
>Does this by scraping last access time on the bin_in.wav (bin installed sound). 

>Will pop up in home-assistant under the same device as your exisiting valetudo MQTT-device, given that the same "DEVICENAME" is used between this and valetudo!
#### Config variables:
| Variable name  |  Description | Default value  | Required |
|---|---|---|---|
| DEVICENAME | Name of the device in homeassistant | roborock | No |
| ROBOROCKHOST  |  Hostname or IP of vacuum |  X | Yes |
|  SSHUSER | SSH Username  |  root | No |
| LANGUAGE  | Valetudo language, used to get correct wav file | en | No|
|  MQTTHOST | MQTT Hostname or IP  | X  | Yes| 
|  MQTTPORT |  MQTT Port  | 1883  | No|
| MQTTUSERNAME  |  Mqtt username | iot  | Probably |
| MQTTPASSWORD  |  MQTT Password |  changeme | No | 
| MQTTCLIENTNAME  |  MQTT Client identifier |  bin2mqtt | No | 

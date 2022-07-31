# roborock-bin2mqtt

## Simple python script to scrape last time dustbin was cycled from valetudo-enabled vacuums, and push to MQTT (Home assistant support) (tested on S50)
>Does this by scraping last access time on the bin_in.wav (bin installed sound). 

>Will pop up in home-assistant under the same device as your exisiting valetudo MQTT-device, given that the same "DEVICENAME" is used between this and valetudo!
### K8s setup
#### Setup - Required secrets
```
export namespace='<your-namespace>'

kubectl -n $namespace create secret generic bin2mqtt-secret --from-literal=DEVICENAME=<yourdevicename> --from-literal=ROBOROCKHOST=<vauum-host> --from-literal=MQTTHOST=<mqtt-host> --from-literal=MQTTPASSWORD=<mqtt-password> --from-literal=MQTTUSER=<mqtt-user>

kubectl -n $namespace create secret generic ssh-key --from-file=robokey=<path-to-key>
```
#### Installation - GitOps
- Install required secrets^
- Point your gitops tool (argocd/flux) to the `k8s/deployment` folder

#### Installation - Manual
- Install required secrets^
- `kubectl -n $namespace apply -f deployment/cronjob.yaml`
### Docker setup
- Make a cronjob on your host:
    - Change crontab with:    
        - `sudo crontab -e` 
        
         or 

        - `crontab -e` if your user is part of docker group  

    - Add the following line:
        
        `05 */6 * * * docker run -e DEVICENAME=<yourdevicename> -e ROBOROCKHOST=<vauum-host> -e MQTTHOST=<mqtt-host> -e MQTTPASSWORD=<mqtt-password> -e MQTTUSER=<mqtt-user> ghcr.io/dbeltman/roborock-bin2mqtt:develop`
> Use [crontab.guru](https://crontab.guru/#05_*/6_*_*_*) to make a cronjob yourself, with explainations and schedules.

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

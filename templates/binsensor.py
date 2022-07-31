import os

device_name = os.getenv('DEVICENAME', 'Roborock')
binsensor_name = os.getenv('SENSORNAME', device_name + '-binsensor')
binsensor_topic = os.getenv('BINSTATETOPIC', '' + device_name + '/last-empty-date')

binsensor_config_template = {
    "name": binsensor_name,
    "unique_id": binsensor_name.lower(),
    "device": {
        "manufacturer": "Roborock",
        "model": "S50",
        "name": device_name,
        "identifiers": [
            device_name.lower()
        ],
        "sw_version": "0.1"
    },
    "state_topic": binsensor_topic
}
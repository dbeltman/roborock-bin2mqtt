import components.mqtt_controller as mqtt_controller

mqtt_controller.init_connect()
mqtt_controller.publish_config()
mqtt_controller.publish_metrics()


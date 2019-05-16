import time
import random
import paho.mqtt.client as mqtt
from fiotclient.iot import FiwareIotClient

DEVICE_ID = 'SPLACE001'
MQTT_BROKER_ADDRESS = 'fiwarelab.rnp.br'
MQTT_BROKER_PORT = 8005

SERVICE_NAME = 'UFRN'
SERVICE_PATH = '/dimap'
SERVICE_API_KEY = '172c602a76ad11e9b2760242ac110007'


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/{}/{}/cmd".format(SERVICE_API_KEY, DEVICE_ID))


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    topic = msg.topic
    incoming_message = msg.payload.decode("utf-8")  # ex: SPLACE001@change_state_ac|ON

    splitted_incoming_message = incoming_message.split('@')
    device_id = splitted_incoming_message[0]
    cmd = splitted_incoming_message[1]
    splitted_cmd = cmd.split('|')
    cmd_name = splitted_cmd[0]
    cmd_param = splitted_cmd[1]

    response_topic = topic + 'exe'
    payload_response_ok = '{}@{}|{}'.format(device_id, cmd_name, 'SUCCESS')
    payload_response_error = '{}@{}|{}'.format(device_id, cmd_name, 'ERROR')

    if cmd_name == 'change_state_ac':
        print('Running command change_state_ac')
        if cmd_param == 'ON':
            print('Change state to ON')
            client.publish(response_topic, payload_response_ok)
        elif cmd_param == 'OFF':
            print('Change state to OFF')
            client.publish(response_topic, payload_response_ok)
        else:
            print('Unknown parameter')
            client.publish(response_topic, payload_response_error)
    else:
        print('Unknown command')
        client.publish(response_topic, payload_response_error)


mqtt_client = mqtt.Client()
mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

mqtt_client.connect(MQTT_BROKER_ADDRESS, MQTT_BROKER_PORT, 60)

mqtt_client.loop_start()

iot_client = FiwareIotClient.from_config_file("config.ini")
iot_client.set_service(SERVICE_NAME, SERVICE_PATH)
iot_client.set_api_key(SERVICE_API_KEY)

while True:
    presence = bool(random.getrandbits(1))
    temperature = random.randint(15, 40)
    humidity = random.randint(50, 100)

    payload = {'t': temperature, 'h': humidity, 'p': presence}
    print('publish {}'.format(payload))

    iot_client.send_observation(DEVICE_ID, payload, protocol='MQTT')

    time.sleep(5)                    # wait for 5 seconds

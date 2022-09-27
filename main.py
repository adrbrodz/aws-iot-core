# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: MIT-0

from awscrt import io, mqtt, auth, http
from awsiot import mqtt_connection_builder
import time as t
import json

# Define ENDPOINT, CLIENT_ID, PATH_TO_CERTIFICATE, PATH_TO_PRIVATE_KEY, PATH_TO_AMAZON_ROOT_CA_1,
# MESSAGE, TOPIC, and RANGE
ENDPOINT = "a2uj790guuziv0-ats.iot.eu-central-1.amazonaws.com"  # Always the same across all IoT Core implications
CLIENT_ID = "1"                                                 # ID of the device running this script
PATH_TO_CERTIFICATE = \
    "certificates/c54590da95f0aac7c2d55db4a6f580aa6a232b2c3" \
    "de0d5d43c2fd44acc3e4728-certificate.pem.crt"               # Path to the IoT Thing's certificate
PATH_TO_PRIVATE_KEY = \
    "certificates/c54590da95f0aac7c2d55db4a6f580aa6a232b2c3" \
    "de0d5d43c2fd44acc3e4728-private.pem.key"                   # Path to the IoT Thing's private key
PATH_TO_AMAZON_ROOT_CA_1 = \
    "certificates/root.pem"                                     # Path to the AMAZON_ROOT_CA_1 certificate
MESSAGE = {                                                     # MQTT message to be published to IoT Core (JSON)
    'measurement_01': 2000,
    'measurement_02': 2100,
    'measurement_03': 1900
}
TOPIC = "device/1/data"                                         # MQTT topic to be published on
RANGE = 1                                                       # How many times the message should be published

# Spin up resources
event_loop_group = io.EventLoopGroup(1)
host_resolver = io.DefaultHostResolver(event_loop_group)
client_bootstrap = io.ClientBootstrap(event_loop_group, host_resolver)
mqtt_connection = mqtt_connection_builder.mtls_from_path(
    endpoint=ENDPOINT,
    cert_filepath=PATH_TO_CERTIFICATE,
    pri_key_filepath=PATH_TO_PRIVATE_KEY,
    client_bootstrap=client_bootstrap,
    ca_filepath=PATH_TO_AMAZON_ROOT_CA_1,
    client_id=CLIENT_ID,
    clean_session=False,
    keep_alive_secs=6
)
print("Connecting to {} with client ID '{}'...".format(
    ENDPOINT, CLIENT_ID))
# Make the connect() call
connect_future = mqtt_connection.connect()
# Future.result() waits until a result is available
connect_future.result()
print("Connected!")
# Publish message to server desired number of times.
print('Begin Publish')
for i in range(RANGE):
    mqtt_connection.publish(topic=TOPIC, payload=json.dumps(MESSAGE), qos=mqtt.QoS.AT_LEAST_ONCE)
    t.sleep(0.1)
print('Published message: {} to the topic {}.'.format(MESSAGE, TOPIC))
print('Publish End')
disconnect_future = mqtt_connection.disconnect()
disconnect_future.result()

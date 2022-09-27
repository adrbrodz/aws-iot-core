# Publishing MQTT messages to AWS  IoT Core

## 1. Preparation
Install the AWS IoT SDK for Python v2 by running the following from the command line:

```
pip install awsiotsdk
```

Install the related dependencies by running the following from the command line:

```
pip install requests
```
## 2. Usage
To publish a preset MQTT message to the IoT Core run the following from the command line:

```
python3 main.py
```

To pass your own arguments run the following from the command line:

```
publish.py --endpoint ENDPOINT --cert CERT --key KEY --topic TOPIC [--message MESSAGE]
```

### Arguments
- --endpoint ENDPOINT: AWS IoT Core endpoint

- --cert CERT: path to the IoT Thing's certificate
- --key KEY: path to the IoT Thing's private key
- --topic TOPIC: topic to be published to
- [--message MESSAGE]: MQTT message to be published 

For example the following code publishes a 'Hello World' message to devices/1/data:

```
python3 publish.py --endpoint a2uj790guuziv0-ats.iot.eu-central-1.amazonaws.com
--cert certificates/c54590da95f0aac7c2d55db4a6f580aa6a232b2c3de0d5d43c2fd44acc3e4728-certificate.pem.crt
--key certificates/c54590da95f0aac7c2d55db4a6f580aa6a232b2c3de0d5d43c2fd44acc3e4728-private.pem.key
--topic device/1/data --message 'Hello World'
```
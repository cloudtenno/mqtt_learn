import paho.mqtt.client as mqtt

# Define the MQTT broker (replace with your broker's address)
broker_address = "mqtt_broker_address"
port = 1883

# Create a unique client ID
client_id = "unique_client_id"

# Create a MQTT client instance
client = mqtt.Client(client_id)

# Connect to the broker
client.connect(broker_address, port)

print(client)

# Define the topic and message to be sent
topic = "/test"
message = "Hello, MQTT!"

# Publish the message to the specified topic
client.publish(topic, message)

# Disconnect from the broker
client.disconnect()

import paho.mqtt.client as mqtt

# Define the MQTT broker (replace with your broker's address)
broker_address = "mqtt_broker_address"
port = 1883

# Create a unique client ID
client_id = "unique_client_id"

# Create a MQTT client instance
client = mqtt.Client(client_id)

# Callback function to be called when a message is received
def on_message(client, userdata, msg):
    print(f"Received message on topic {msg.topic}: {msg.payload.decode()}")

# Set the callback function
client.on_message = on_message

# Connect to the broker
client.connect(broker_address, port)

# Define the topic to subscribe to
topic = "/test"

# Subscribe to the specified topic
client.subscribe(topic)

# Start the loop to listen for incoming messages
client.loop_forever()

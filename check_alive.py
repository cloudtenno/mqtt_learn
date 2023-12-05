import paho.mqtt.client as mqtt
import time

def check_mqtt_server(broker_address, port):
    client_id = "mqtt_server_tester"
    client = mqtt.Client(client_id)

    try:
        # Connect to the broker
        client.connect(broker_address, port)

        # Start the loop and wait for a brief moment
        client.loop_start()
        time.sleep(2)  # Adjust the sleep duration as needed

        # Check if the client is still connected
        if client.is_connected():
            print("MQTT server is alive.")
        else:
            print("MQTT server is not responding.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Stop the loop and disconnect from the broker
        client.loop_stop()
        client.disconnect()

# Replace with your MQTT broker's address and port
mqtt_broker_address = "mqtt_broker_address"
mqtt_port = 1883

# Test the MQTT server
check_mqtt_server(mqtt_broker_address, mqtt_port)

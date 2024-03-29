from fastapi_mqtt import FastMQTT


def start_mqtt(mqtt: FastMQTT) -> None:
    @mqtt.on_connect()
    def connect(client, flags, rc, properties):
        mqtt.client.subscribe("/mqtt")  # subscribing mqtt topic
        print("Connected: ", client, flags, rc, properties)

    @mqtt.on_message()
    async def message(client, topic, payload, qos, properties):
        print("Received message: ", topic, payload.decode(), qos, properties)

    @mqtt.subscribe("my/mqtt/topic/#")
    async def message_to_topic(client, topic, payload, qos, properties):
        print(
            "Received message to specific topic: ",
            topic,
            payload.decode(),
            qos,
            properties,
        )

    @mqtt.on_disconnect()
    def disconnect(client, packet, exc=None):
        print("Disconnected")

    @mqtt.on_subscribe()
    def subscribe(client, mid, qos, properties):
        print("subscribed", client, mid, qos, properties)

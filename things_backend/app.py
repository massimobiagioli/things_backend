from functools import lru_cache

from fastapi import FastAPI
from fastapi_mqtt import MQTTConfig, FastMQTT

from things_backend.mqtt import start_mqtt
from things_backend.routes import health, tester
from things_backend.settings import Settings

app = FastAPI()


@lru_cache
def get_settings() -> Settings:
    return Settings()


def get_mqtt_config() -> MQTTConfig:
    settings = get_settings()

    return MQTTConfig(
        host=settings.mqtt_broker_host,
        port=settings.mqtt_broker_port,
        username=settings.mqtt_broker_user,
        password=settings.mqtt_broker_password,
    )


mqtt = FastMQTT(config=get_mqtt_config())

mqtt.init_app(app)

app.include_router(health.router)
app.include_router(tester.router)

start_mqtt(mqtt)

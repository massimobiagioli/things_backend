from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    mqtt_broker_host: str
    mqtt_broker_port: int = 1883
    mqtt_broker_user: Optional[str] = None
    mqtt_broker_password: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env")

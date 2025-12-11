from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    BOT_TOKEN: str

    API_TITLE: str = "Partner Bot API"
    API_VERSION: str = "1.0.0"

    class Config:
        env_file = ".env"
        extra = "allow"


settings = Settings()

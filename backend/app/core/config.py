from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # 🔐 JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # 🗄 Database
    DATABASE_URL: str

    class Config:
        env_file = ".env"
        extra = "ignore"  # prevents crash if extra env vars exist


settings = Settings()

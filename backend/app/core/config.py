from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    This class reads settings from environment variables or a .env file.
    It provides a single, type-safe 'settings' object.
    """
    
    # Database URL
    # Pydantic will automatically look for an environment variable
    # named 'DATABASE_URL' (case-insensitive).
    DATABASE_URL: str

    # JWT (Login Token) Settings
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str

    # This 'Config' class tells Pydantic to look for a .env file
    # in the parent directory (relative to this file)
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

# Create a single instance of the settings to be imported
# by other parts of the application.
settings = Settings()


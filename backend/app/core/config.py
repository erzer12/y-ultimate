"""
Configuration Management using Pydantic Settings

This file defines the Settings class that manages all application configuration.
It automatically reads values from:
  1. Environment variables (e.g., DATABASE_URL, JWT_SECRET_KEY)
  2. A .env file in the root directory (if it exists)

The BaseSettings class from pydantic_settings handles this automatically.
Once you create an instance of Settings(), you get a single, type-safe
object containing all your configuration values.

This pattern is superior to manually reading environment variables because:
  - Type validation: Pydantic ensures values are the correct type
  - Default values: You can specify fallback values if env vars are missing
  - Documentation: The class itself documents what configuration is needed
  - Single source of truth: All settings are in one place
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Application Settings
    
    All attributes will be automatically populated from environment variables
    or from a .env file. For example, DATABASE_URL will be read from the
    DATABASE_URL environment variable.
    """
    
    # === Database Configuration ===
    # The full database connection string (e.g., "postgresql://user:password@localhost:5432/dbname")
    DATABASE_URL: str
    
    # === JWT (JSON Web Token) Configuration ===
    # A secret key used to sign JWT tokens. MUST be kept secret.
    # Generate this with: openssl rand -hex 32
    JWT_SECRET_KEY: str
    
    # The algorithm used for signing JWT tokens (HS256 is standard)
    JWT_ALGORITHM: str = "HS256"
    
    # How long (in minutes) the access token is valid before expiring
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

    class Config:
        """
        Pydantic configuration class
        
        env_file: Tells Pydantic to read from a .env file
        case_sensitive: Environment variable names must match exactly (e.g., DATABASE_URL, not database_url)
        """
        env_file = ".env"
        case_sensitive = True


# Create a single, global instance of the settings
# This instance will be imported and used throughout the application
settings = Settings()

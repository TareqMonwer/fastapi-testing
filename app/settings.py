import enum
import os

from pydantic import BaseSettings
from yarl import URL


class LogLevel(str, enum.Enum):  # noqa: WPS600
    """Possible log levels."""

    NOTSET = "NOTSET"
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    FATAL = "FATAL"


class Settings(BaseSettings):
    """
    Application settings.

    These parameters can be configured
    with environment variables.
    """

    host: str = "127.0.0.1"
    port: int = 8000
    # quantity of workers for uvicorn
    workers_count: int = 1
    # Enable uvicorn reloading
    reload: bool = False

    # Current environment
    environment: str = "dev"

    log_level: LogLevel = LogLevel.INFO

    # Variables for the database
    db_name: str
    db_host: str
    db_user: str
    db_passwd: str
    db_echo: bool = False

    @property
    def db_url(self) -> URL:
        """
        Assemble database URL from settings.

        :return: database URL.
        """
        url = URL.build(
            scheme="mssql+pyodbc",
            user=self.db_user,
            password=self.db_passwd,
            host=self.db_host,
        )
        url = url.with_path("/" + self.db_name)
        url = url.with_query("driver=ODBC+Driver+17+for+SQL+Server")
        return url

    class Config:
        env_file = ".env"
        env_prefix = "APP_"
        env_file_encoding = "utf-8"


settings = Settings()

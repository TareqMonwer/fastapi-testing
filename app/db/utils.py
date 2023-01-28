import os

from app.settings import settings


def create_database() -> None:
    """Create a databse."""


def drop_database() -> None:
    """Drop current database."""
    if settings.db_file.exists():
        os.remove(settings.db_file)

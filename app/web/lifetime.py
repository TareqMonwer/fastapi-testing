from typing import Awaitable, Callable

from fastapi import FastAPI
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

from app.settings import settings


def _setup_db(app: FastAPI) -> None:  # pragma: no cover
    """
    Creates connection to the database.

    This function creates SQLAlchemy engine instance,
    session_factory for creating sessions
    and stores them in the application's state property.

    :param app: fastAPI application.
    """
    engine = create_engine(str(settings.db_url), echo=settings.db_echo)
    session_factory = sessionmaker(
            engine,
            expire_on_commit=False,
            class_=Session,
        )
    app.state.db_engine = engine
    app.state.db_session_factory = session_factory


def register_startup_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application startup.

    This function uses fastAPI app to store data
    inthe state, such as db_engine.

    :param app: the fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("startup")
    def _startup() -> None:  # noqa: WPS430
        print(".... Connecting to the Database ...")
        _setup_db(app)
        print(".... Conection successful ...")
        pass  # noqa: WPS420

    return _startup


def register_shutdown_event(
    app: FastAPI,
) -> Callable[[], Awaitable[None]]:  # pragma: no cover
    """
    Actions to run on application's shutdown.

    :param app: fastAPI application.
    :return: function that actually performs actions.
    """

    @app.on_event("shutdown")
    def _shutdown() -> None:  # noqa: WPS430
        app.state.db_engine.dispose()

        pass  # noqa: WPS420

    return _shutdown

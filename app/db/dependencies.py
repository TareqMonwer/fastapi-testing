from app import session
from starlette.requests import Request
from sqlalchemy.orm import Session


def get_db_session(request: Request) -> Session:
    """
    Create and get database session.

    :param request: current request.
    :yield: database session.
    """
    db = session.SessionLocal()

    try:  # noqa: WPS501
        yield db
    finally:
        db.commit()
        db.close()

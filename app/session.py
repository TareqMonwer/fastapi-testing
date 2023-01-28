from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings


engine = create_engine(str(settings.db_url), pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

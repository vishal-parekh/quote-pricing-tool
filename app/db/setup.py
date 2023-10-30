from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database


SQLALCHEMY_DATABASE_URL = "postgresql://localhost/dev-sure"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
if not database_exists(engine.url):
    print(database_exists(engine.url))

    create_database(engine.url)
print(database_exists(engine.url))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Session = SessionLocal()
Base = declarative_base()

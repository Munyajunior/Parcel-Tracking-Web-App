from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv

load_dotenv()

db_user: str = os.getenv("USER")
db_port: int = os.getenv("PORT")
db_host: str = os.getenv("HOST")
db_password: str = os.getenv("PASS")
db_domain: str = os.getenv("DOMAIN")
db_name: str = os.getenv("DB_NAME")

# Database URL from environment variables
DATABASE_URL: str = f'{db_domain}://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./health.db"

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()
#engine, SessionLocal, and Base is called upon in main.py
#SessionLocal becomes db
#Base creates a class/table allowing for the template/structure of a database

#TODO: Find something to expand on (database? backend logic? More factors? Accounts?)
#TODO: Add more factors (diet, lifestyle, 13-24 age)
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker
from databases import Database
import os

# Environment variables for MySQL connection (replace with your actual credentials)
SQLALCHEMY_DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqldb://u404361482_umusaruro:Niyokwizera1$@193.203.166.183:3306/u404361482_umusarurohub")

# For async usage
database = Database(SQLALCHEMY_DATABASE_URL)

# SQLAlchemy engine for sync queries
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Session local for database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine,class_=AsyncSession)


# Base class for model declarations
Base = declarative_base()

# Dependency to get the database session for routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

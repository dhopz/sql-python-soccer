# Import the modules required
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

# PostgreSQL Database credentials loaded from the .env file
DATABASE = os.getenv('DATABASE')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


# Create the engine
engine = create_engine("postgresql+psycopg2://"+DATABASE_USERNAME+":postgres@localhost/soccer")

# Initialize the session
session = Session(engine)

# Initialize the declarative base
Base = declarative_base()
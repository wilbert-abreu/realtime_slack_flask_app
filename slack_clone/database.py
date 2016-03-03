from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
from slack_clone import app

engine = create_engine(os.environ["DATABASE_URL"])
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

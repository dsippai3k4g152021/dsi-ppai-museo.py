import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

engine = create_engine('sqlite:///museo.sqlite', echo=True)

Base = declarative_base()

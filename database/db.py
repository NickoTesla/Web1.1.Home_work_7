from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
url = f'postgresql://postgres:55555@localhost:5432/postgres'
engine = create_engine(url)
Base = declarative_base()
Session = sessionmaker(bind=engine)

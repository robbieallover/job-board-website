from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create an engine to connect to the database
engine = create_engine('sqlite:///jobs.db')

# Create a session factory
Session = sessionmaker(bind=engine)

# Create a session instance
session = Session()

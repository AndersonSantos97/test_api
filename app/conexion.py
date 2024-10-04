from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABSE_URL = "mysql+mysqldb://root:Anderson0501@localhost:3306/important_data"

engine = create_engine(DATABSE_URL)

SessionLocal = sessionmaker(autocommit = False, autoflush = False, bind = engine)

Base = declarative_base()
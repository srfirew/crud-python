from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

BANCO_URL = "mysql+mysqlconnector://root:1908@localhost:3306/python_crud_banco"

db = create_engine(BANCO_URL)

Session = sessionmaker(bind=db)
session = Session()

Base = declarative_base()




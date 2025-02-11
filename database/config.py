from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from database import Base


engine = create_engine('sqlite:///database/banco.db')
session = Session(bind=engine)
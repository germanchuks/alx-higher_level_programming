#!/usr/bin/python3
""" Module that contains class definition of State and an instance Base """

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ State class representing the states table """
    __tablename__ = 'states'
    id = Column(Integer, autoincrement=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)

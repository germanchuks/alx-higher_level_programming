#!/usr/bin/python3
""" Prints all City objects from the database hbtn_0e_14_usa """

from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).order_by(City.id).all()

    for obj in states:
        print(f"{obj[0]}: ({obj[1]}) {obj[2]}")

    session.close()

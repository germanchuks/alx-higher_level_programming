#!/usr/bin/python3
""" Adds the State object “Louisiana” to the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    new_state_obj = session.query(State).filter(State.name == 'Louisiana').\
        first()
    print(new_state_obj.id)

    session.close()

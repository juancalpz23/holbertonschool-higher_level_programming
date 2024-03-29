#!/usr/bin/python3
"""
List all obj that contain letter a
Takes 3 args
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state = (session.query(State).order_by(State.id).
             filter(State.name.like('%a%')))
    for states in state:
        print("{}: {}".format(states.id, states.name))
    session.close()

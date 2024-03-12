#!/usr/bin/python3
"""
Prints the State object with the name passed as 
argument from the database hbtn_0e_6_usa
Takes 4 arguments
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
             filter(State.name.like(argv[4])).first())
    if state:
        print(state.id)
    else:
        print("Not found")
    session.close()

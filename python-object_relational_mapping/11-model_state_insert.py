#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the
database hbtn_0e_6_usa
Takes 3 args
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    column = State(name="Louisiana")
    session.add(column)
    session.commit()
    state = session.query(State).order_by(State.id.desc()).first()
    print(state.id)
    session.close()

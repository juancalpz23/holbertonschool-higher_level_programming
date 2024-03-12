#!/usr/bin/python3
"""
List all obj that contain letter a
Takes 3 args
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    state = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id).all()
    if state:
        for st in state:
            if 'a' in st.name:
                print("{}: {}".format(st.id, st.name))
    session().close()
#!/usr/bin/python3

"""
script lists state objects from database
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    username, password, database = sys.argv[1:4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    mysession = sessionmaker(bind=engine)
    session = mysession()
    for state in session.query(State):
        print("{}: {}".format(state.id, state.name))
    session.close()

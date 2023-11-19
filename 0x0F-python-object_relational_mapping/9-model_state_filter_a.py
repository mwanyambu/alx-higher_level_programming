#!/usr/bin/python3

"""
script lists all states that have letter 'a' in them
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    mysession = sessionmaker(bind=engine)
    session = mysession()
    for state in session.query(State).filter(State.name.like('%a%')):
        print("{}: {}".format(state.id, state.name))
    session.close()

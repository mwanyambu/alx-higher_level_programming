#!/usr/bin/python3

"""
script inserts a new state
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
    state = State(name="Lousiana")
    session.add(state)
    session.commit()
    print(state.id)
    session.close()

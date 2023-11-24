#!/usr/bin/python3

"""
prints all cities names
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine, ForeignKey
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    mysession = sessionmaker(bind=engine)
    session = mysession()
    for state, city in session.query(State, City).join(City):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()

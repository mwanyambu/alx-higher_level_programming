#!/usr/bin/python3

"""
script creates state and city from database
"""


import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}: {}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    mysession = sessionmaker(bind=engine)
    session = mysession()
    for state in session.query(State):
        for city in statte.city:
            print("{:d}: {} -> {}".format(city.id, city.name, state.name))
    session.close()

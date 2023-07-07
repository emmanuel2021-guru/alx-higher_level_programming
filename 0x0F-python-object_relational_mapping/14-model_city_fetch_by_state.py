#!/usr/bin/python3

"""This script prints all 'City' objects from the database 'hbtn_0e_14_usa'"""

from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    for state_inst, city_inst in session.query(State, City)\
            .join(City, State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(state_inst.name,
              city_inst.id, city_inst.name))

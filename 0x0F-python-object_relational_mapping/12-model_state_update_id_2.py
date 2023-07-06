#!/usr/bin/python3

"""This script changes the name of a 'State'
object from the database 'hbtn_0e_6_usa'"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_upd = session.query(State).filter_by(id='2').first()
    state_upd.name = 'New Mexico'
    session.commit()

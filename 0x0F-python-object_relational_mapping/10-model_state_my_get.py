#!/usr/bin/python3

"""This script prints the 'State' object with the 'name' passed as argument
from the database 'hbtn_0e_6_usa'"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4].split(";")
    if session.query(State).filter(State.name == state_name[0]).first()\
            is None:
        print("Not Found")
    else:
        for instance in session.query(State)\
                .filter(State.name == state_name[0]):
            print(instance.id)

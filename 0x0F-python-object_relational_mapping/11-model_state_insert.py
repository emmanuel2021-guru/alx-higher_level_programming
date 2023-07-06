#!/usr/bin/python3

"""This script adds the 'State' object
'Louisiana' to the database 'hbtn_0e_6_usa'"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    new_user = State(name='Louisiana')
    session.add(new_user)
    session.commit()
    print(new_user.id)

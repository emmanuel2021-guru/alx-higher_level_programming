#!/usr/bin/python3

"""This file contains the class definition of a State and an instance
Base = declarative_base()"""


from sqlalchemy import Integer, String, Column, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class definition of a state instance"""
    __tablename__ = "states"

    id = Column(Integer, autoincrement=True, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

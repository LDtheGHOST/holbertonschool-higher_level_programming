#!/usr/bin/python3
"""
        Implement a class State that inherits from Base
        linked to 'states' table of MySQL server
        MySQL server running on localhost port 3306
"""
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class State(Base):
    """State class inheriting from Base."""
    __tablename__ = 'states'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False
        )
    name = Column(
        String(128),
        nullable=False
        )
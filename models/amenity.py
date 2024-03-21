#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy import CHAR, DateTime,func
from sqlalchemy.ext.declarative import declarative_base
from models.state import State
from sqlalchemy.orm import relationship, backref


class Amenity(BaseModel):
    __tablename__ = 'cities'
    name = Column(String(128), nullable=False)

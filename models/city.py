#!/usr/bin/python3
"""
City Module for HBNB project
will be used to map to cities table

"""
import models
from datetime import datetime
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """
    The city class, contains state ID and name
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        id = Column(String(60), primary_key=True, nullable=False)
        created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade="all, delete", backref="cities")
    else:
        state_id = ""
        name = ""

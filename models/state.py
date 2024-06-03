#!/usr/bin/python3
"""State module for HBNB project"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Relationship for DBStorage
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """Return the list of City objects from storage linked to the current State"""
        if models.storage_t != 'db':
            from models.city import City  # Delayed import to avoid circular dependency
            return [city for city in models.storage.all(City).values() if city.state_id == self.id]

from sqlalchemy import Column, String, DateTime
from src.database import Base

class Driver(Base):
    """Drivers Table"""

    __tablename__ = 'drivers'
    name = Column(String(80), nullable=False, primary_key=True)
    current_location = Column(String(100), nullable=False)
    destination = Column(String(100), nullable=False)
    timestamp = Column(DateTime, nullable=False)

    def __repr__(self):
        """String representation of the Driver object."""
        return f'Driver [name={self.name}, location={self.current_location}, destination={self.destination}, time={self.timestamp}]'

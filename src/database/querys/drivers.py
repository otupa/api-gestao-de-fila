from typing import List

from src.database.db_connection import db_connector
from src.database.models.drivers import Driver


class DriverQuerys:
    """CRUD operations for the Driver entity"""

    @classmethod
    @db_connector
    def create(cls, connection, name: str, current_location: str, destination: str) -> None:
        """Create a new driver in the queue"""
        driver = Driver(name=name, current_location=current_location, destination=destination)
        connection.session.add(driver)
        connection.session.commit()

    @classmethod
    @db_connector
    def get_all(cls, connection) -> List[Driver]:
        """Get a list with all drivers in the queue"""
        return connection.session.query(Driver).all()

    @classmethod
    @db_connector
    def get_by_name(cls, connection, name: str) -> Driver:
        """Get a driver by their name"""
        return connection.session.query(Driver).filter_by(name=name).first()

    @classmethod
    @db_connector
    def update_location_and_destination(cls, connection, name: str, new_location: str, new_destination: str) -> None:
        """Update the current location and destination of a driver"""
        driver = connection.session.query(Driver).filter_by(name=name).first()
        if driver:
            driver.current_location = new_location
            driver.destination = new_destination
            connection.session.commit()

    @classmethod
    @db_connector
    def delete(cls, connection, name: str) -> None:
        """Remove a driver from the queue by their name"""
        driver = connection.session.query(Driver).filter_by(name=name).first()
        if driver:
            connection.session.delete(driver)
            connection.session.commit()

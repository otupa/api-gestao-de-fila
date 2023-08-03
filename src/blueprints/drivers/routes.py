from flask import Blueprint, jsonify, request
from src.database.querys import DriverQuerys

drivers_app = Blueprint('drivers_app', __name__, url_prefix='/api/drivers')

@drivers_app.route('/', methods=['GET'])
def get_all_drivers():
    """Get all drivers."""
    drivers = DriverQuerys.get_all()
    return jsonify(drivers=[driver.serialize() for driver in drivers])
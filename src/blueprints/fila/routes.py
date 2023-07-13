# pylint: disable=no-value-for-parameter
"""Clientes"""

from flask import Blueprint, jsonify


fila = Blueprint('fila', __name__, url_prefix='/')


@fila.route('/')
def show():
    """Retorna para o chatbot que a api esta funcionando"""

    return jsonify(
        motorista="marcos",
        embarque = "rua dos andradas, 149")

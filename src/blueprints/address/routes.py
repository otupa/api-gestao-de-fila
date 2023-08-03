import os
from flask import Blueprint, jsonify, request
import requests

address_app = Blueprint('address_app', __name__, url_prefix='/api/address')

def verify_address(address):
    """Verifica a validade de um endereço usando a API do Google Geocoding.

    Args:
        address (str): O endereço a ser verificado.
        api_key (str): A chave de API do Google Geocoding.

    Returns:
        dict: Um dicionário contendo a resposta da API do Google Geocoding.
    """
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    params = {
        "address": address,
        "key": os.environ.get("API_MAPS_KEY")
    }

    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    return data

@address_app.route('/verify_address', methods=['GET'])
def check_address():
    """Verifica a validade de um endereço fornecido no corpo da requisição JSON.

    Returns:
        json: Uma resposta JSON contendo a validade do endereço e uma mensagem.
    """
    data = request.get_json()
    address = "sdf"

    if address:
        response_data = verify_address("rua dos andradas, 149, sao lourenco")
        if response_data.get('status') == 'OK':
            return jsonify({'valid': True, 'message': 'O endereço é válido.', 'responde:':response_data}), 200
        else:
            return jsonify({'valid': False, 'message': 'O endereço é inválido.'}), 400
    else:
        return jsonify({'error': 'O endereço não foi fornecido.'}), 400

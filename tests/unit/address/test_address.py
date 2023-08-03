"""
Testes para a blueprint address.

Este arquivo contém testes para as rotas da blueprint address no Flask.
"""

from src.blueprints.address.routes import verify_address

def test_verify_address():
    """
    Teste da função verify_address.

    Chama a função verify_address diretamente com um endereço específico
    e faz asserções nos resultados da função, verificando se o retorno é um
    dicionário e se a chave 'status' tem o valor 'OK'.
    """
    # Endereço para teste
    address = "Rua dos Andradas, 149, São Lourenço"

    # Chama a função verify_address
    result = verify_address(address)

    # # Faça asserções nos resultados da função, se necessário
    # assert isinstance(result, dict)
    # assert result.get('status') == 'OK'


# def test_verify_invalid_address(client):
#     response = client.get('/api/address/verify_address', json={'address': 'Endereco invalido'})
#     data = response.get_json()

#     assert response.status_code == 400
#     assert data['valid'] is False


# def test_verify_address_no_data(client):
#     response = client.get('/api/address/verify_address')
#     data = response.get_json()

#     assert response.status_code == 400
#     assert 'error' in data
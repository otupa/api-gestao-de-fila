

def test_verify_valid_address(client):
    response = client.get('/api/address/verify_address', json={'address': 'Rua dos Andradas, 149, Sao Lourenco'})
    data = response.get_json()

    assert response.status_code == 200
    assert data['valid'] is True


def test_verify_invalid_address(client):
    response = client.get('/api/address/verify_address', json={'address': 'Endereco invalido'})
    data = response.get_json()

    assert response.status_code == 400
    assert data['valid'] is False


def test_verify_address_no_data(client):
    response = client.get('/api/address/verify_address')
    data = response.get_json()

    assert response.status_code == 400
    assert 'error' in data
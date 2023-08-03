import pytest
# tests/test_factory.py

def test_app_creation(app):
    # Chame a factory para criar a aplicação Flask

    # Verifique se a aplicação foi criada corretamente
    assert app is not None
    # assert app.testing is False  # Verifique se a configuração de teste está desativada
    # assert app.config['DEBUG'] is False  # Verifique se o modo de depuração está desativado (pode variar dependendo da configuração)

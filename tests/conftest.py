
import pytest

from src import init_app

@pytest.fixture(scope="module")
def app():
    """Fixture para criar a instância da aplicação Flask."""
    app = init_app()
    yield app

@pytest.fixture(scope="module")
def client(app):
    """Fixture para criar um cliente de teste para a aplicação."""
    return app.test_client()

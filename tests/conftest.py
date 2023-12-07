import pytest
from fastapi.testclient import TestClient

from things_backend.main import app


@pytest.fixture(scope="function")
def client():
    return TestClient(app)

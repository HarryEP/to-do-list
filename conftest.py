'''conftest'''

import pytest
from app import app

@pytest.fixture
def test_api():
    return app.test_client()
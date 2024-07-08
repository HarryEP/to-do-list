from unittest.mock import patch


def test_get_home_route_returns_successful_status_code(test_app):

    res = test_app.get("/")

    assert res.status_code == 200

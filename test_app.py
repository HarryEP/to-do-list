from unittest.mock import patch, MagicMock


def test_get_home_route_returns_successful_status_code(test_api):

    res = test_api.get("/")

    assert res.status_code == 200


@patch('app.get_connection')
def test_post_function_returns_successful_status_code(mock_get_connection, test_api):
    mock_conn = MagicMock()
    mock_get_connection.return_value = mock_conn

    new_data = {'item': 'Test Item', 'priority': '1'}
    res = test_api.post("/add_item", data=new_data)

    assert res.status_code == 302
    assert res.location.endswith('/')
    mock_conn.commit.assert_called_once()

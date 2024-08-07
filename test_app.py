from unittest.mock import patch, MagicMock
import psycopg2


def test_get_home_route_returns_successful_status_code(test_api):

    res = test_api.get("/")

    assert res.status_code == 200


@patch('app.get_connection')
def test_post_item_adds_item(mock_get_connection, test_api):
    mock_conn = mock_get_connection.return_value
    mock_cur = mock_conn.cursor.return_value

    new_data = {'item': 'Test Item', 'priority': '1'}
    response = test_api.post("/add_item", data=new_data)

    assert response.status_code == 302
    assert response.location.endswith('/')
    mock_conn.commit.assert_called_once()


@patch('app.get_connection')
def test_completing_an_item(mock_get_connection, test_api):
    mock_conn = MagicMock()
    mock_get_connection.return_value = mock_conn

    response = test_api.post('/complete_item/1')
    assert response.status_code == 302
    assert response.location.endswith('/')
    mock_get_connection.assert_called_once()
    mock_conn.cursor.assert_called_once()


@patch('app.get_connection')
def test_post_item_has_missing_data(mock_get_connection, test_api):
    mock_conn = mock_get_connection.return_value
    mock_cur = mock_conn.cursor.return_value

    new_data = {'item': ''}
    response = test_api.post("/add_item", data=new_data)

    assert response.status_code == 400
    mock_conn.commit.assert_not_called()


@patch('app.get_connection')
def test_deletion_of_item(mock_get_connection, test_api):
    mock_conn = MagicMock()
    mock_get_connection.return_value = mock_conn

    response = test_api.post('/delete_item/1')
    assert response.status_code == 302
    assert response.location.endswith('/')
    mock_get_connection.assert_called_once()
    mock_conn.cursor.assert_called_once()


def test_404(test_api):
    response = test_api.get('/error')
    assert response.status_code == 404
    assert b'Page Not Found' in response.data


@patch('app.get_connection')
def test_500(mock_get_connection, test_api):
    mock_get_connection.side_effect = psycopg2.Error
    response = test_api.get('/')
    assert response.status_code == 500
    assert b'Internal Server Error' in response.data

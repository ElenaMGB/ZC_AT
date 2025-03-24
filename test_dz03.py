import pytest
from main_dz03 import get_catapi_url

def test_get_catapi_url(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://example.com/cat.jpg'}
    ]

    result = get_catapi_url()
    assert result == 'https://example.com/cat.jpg'

def test_get_catapi_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500

    result = get_catapi_url()
    assert result is None

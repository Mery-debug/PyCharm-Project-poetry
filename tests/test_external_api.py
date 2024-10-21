from unittest.mock import patch, Mock
from src.external_api import return_cash


@patch('src.external_api.requests.request')
def test_return_cash(transaction, mock_get) -> None:
    """Test of working func with error (status_code != 200)"""
    mock_get.return_value.json.return_value = {"date": "2024-10-20",
                                               "info": {"rate": 104.205462, "timestamp": 1729464905},
                                               "query": {"amount": 31957.58, "from": "EUR", "to": "RUB"},
                                               "result": 3724.305775, "success": True}
    mock_get.return_value.status_code = 200
    assert return_cash(amount=25, from_currency="USD", to_currency="RUB") == 3724.31


@patch('src.external_api.requests.request')
def test_return_cash1(transaction, mock_get) -> None:
    """Test of working func with error (status_code != 200)"""
    mock_get.return_value.json.return_value = {"date": "2024-10-20",
                                               "info": {"rate": 104.205462, "timestamp": 1729464905},
                                               "query": {"amount": 31957.58, "from": "RUB", "to": "RUB"},
                                               "result": 3724.305775, "success": True}
    mock_get.return_value.status_code = 200
    assert return_cash(amount=25, from_currency="RUB", to_currency="RUB") == 25


@patch('src.external_api.requests.request')
def test_return_cash2(transaction, mock_get) -> None:
    """Test of working func with error (status_code != 200)"""
    mock_get.return_value.json.return_value = {"date": "2024-10-20",
                                               "info": {"rate": 104.205462, "timestamp": 1729464905},
                                               "query": {"amount": 31957.58, "from": "EUR", "to": "RUB"},
                                               "result": 3724.305775, "success": True}
    mock_get.return_value.status_code = 404
    assert return_cash(amount=25, from_currency="USD", to_currency="RUB") == f"Возможная причина {mock_get().reason}"

from unittest.mock import patch, Mock
from src.external_api import return_cash
import requests
from typing import Any


@patch('src.external_api.requests.request')
def test_return_cash(transaction: dict) -> None:
    """Test of working func with error (status_code != 200)"""
    mock_response = Mock()
    requests.request = mock_response
    transaction = {
        'id': 441945886, 'state': 'EXECUTED', 'date': '2019-08-26T10:50:58.294041',
        'operationAmount': {'amount': '31957.58', 'currency': {'name': 'руб.', 'code': 'EUR'}},
        'description': 'Перевод организации', 'from': 'Maestro 1596837868705199', 'to': 'Счет 64686473678894779589'
                  }
    mock_response.return_value.status_code = 200
    assert return_cash(transaction) == 31957.58

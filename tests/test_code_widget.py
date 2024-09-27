from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize('data, expect', [('', ''), ('', ''), ('', '')])
def test_mask_account_card(data, expect):
    assert mask_account_card(data) == expect

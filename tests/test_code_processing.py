from src.processing import sort_by_date


def test_sort_by_date(list_date, expectation):
    assert get_date(sort_by_date) == expectation

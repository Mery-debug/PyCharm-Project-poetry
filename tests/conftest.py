import pytest


@pytest.fixture
def lst():
    return ''


@pytest.fixture
def short():
    return '123456789'


@pytest.fixture
def long():
    return '123456789123456789000000'

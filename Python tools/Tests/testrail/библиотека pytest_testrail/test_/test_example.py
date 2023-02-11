import pytest
from pytest_testrail.plugin import pytestrail


@pytestrail.case('C165')
def test_run():
    assert True


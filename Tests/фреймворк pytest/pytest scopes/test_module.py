# content of test_module.py
import random

import pytest


@pytest.fixture(scope="function")
def smtp_connection():
    return random.randint(34, 56)


def test_ehlo(smtp_connection):
    print(smtp_connection)
    assert False


def test_noop(smtp_connection):
    print(smtp_connection)
    assert False

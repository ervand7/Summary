# Пример теста с помощью pytest
# Configurations: Module name: Test_Something_Pytest.TestSomething
import pytest
from Tests_my_summary.data_for_tests import multiplication_int, multiplication_string


class TestSomething:  # unlike unittest, we do not inherit from anyone

    def setup_class(self):  # this preparatory method runs only 1 time
        print('method setup_class')

    def setup(self):  # we write setup instead setUp
        print("method setup")

    def teardown(self):  # we write teardown instead tearDown
        print("method teardown")

    def test_numbers_3_4(self):
        assert multiplication_int(3, 4) == 12  # we already don't dave assertEqual, only assert

    def test_strings_a_3(self):
        assert multiplication_string('a', 3) == 'aaa'  # we already don't dave assertEqual, only assert

    # we also can check our functions at some parameters
    @pytest.mark.parametrize('first, second, result', [(3, 4, 12), (5, 0, 0), (-5, 10, -50), (2.5, 2, 5.0)])
    def test_numbers(self, first, second, result):
        assert multiplication_int(first, second) == result

    def teardown_class(self):  # this final method runs only 1 time
        print('method teardown_class')

# the order of execution in this case will be following:
# setup_class
# setUp
# test_numbers
# tearDown
# setUp
# test_strings
# tearDown
# teardown_class

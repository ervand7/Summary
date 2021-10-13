# Пример теста с помощью unittest
import unittest
from Tests_my_summary.data_for_tests import multiplication_int, multiplication_string


class TestSomething(unittest.TestCase):  # class TestSomething inheritances from base class TestCase
    def setUp(self):
        # create user
        print("method setUp")

    def tearDown(self):
        # delete user
        print("method tearDown")

    def test_numbers(self):
        self.assertEqual(multiplication_int(3, 4), 12)  # so we have opportunity through method assertEqual
        # check: multiplication_int(3 * 4) = 12
        # So we must know the result (12) of function (3, 4) in advance and write it ((3, 4), 12)
        # inside the following will happen: assert multiplication_int(3, 4) = 12

    def test_strings(self):
        self.assertEqual(multiplication_string('a', 3), 'aaa')  # so we have opportunity through method
        # assertEqual check: multiplication_int('a' * 3) = 'aaa'
        # So we must know the result ('aaa') of function ('a' * 3) in advance and write it (('a', 3), 'aaa')


# the order of execution in this case will be following:
# 1) setUp
# 2) test_numbers
# 3) tearDown
# 4) setUp
# 5) test_strings
# 6) tearDown


if __name__ == '__main__':
    unittest.main()

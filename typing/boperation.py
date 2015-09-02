"""
A B Machine operation.
"""


class BOperation(object):
    """
    Represents a B Operation.
    """

    def __init__(self):
        pass

    def __str__(self):
        return ""

import unittest


class TestBOperation(unittest.TestCase):
    """
    Tests operations.
    """

    def setUp(self):
        pass

    def test_creation(self):
        """
        Tests creation of an element.
        """
        operation = BOperation()
        print operation


if __name__ == '__main__':
    unittest.main()
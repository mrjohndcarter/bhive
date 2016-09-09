"""
A B Machine
"""


class BMachine(object):
    """
    A Synthesized operation.
    """

    def __init__(self, name):
        self.machine_name = name
        self.operations = {}

    def __str__(self):
        return 'Machine: ' + self.machine_name

    def add_operation(self, name, operation):
        self.operations[name] = operation


import unittest


class TestBMachine(unittest.TestCase):
    """
    TestBElement

    Tests BElement.
    """

    def setUp(self):
        pass

    def test_creation(self):
        """
        Tests creation of an element.
        """
        b = BMachine('test_creation')
        print b


if __name__ == '__main__':
    unittest.main()

"""

"""


class BHiveOperation(object):
    def __init__(self, name):
        self.name = name
        self.precondition = None


import unittest


class TestBHiveOperation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        operation = BHiveOperation('myOp')
        assert operation.name == 'myOp'
        assert not operation.precondition


if __name__ == '__main__':
    unittest.main()

"""

"""
import unittest

from mock import Mock


class BHiveOperation(object):
    def __init__(self, name):
        self.name = name
        self.precondition = None

    @staticmethod
    def get_operation_name_from_scenario(scenario):
        return scenario.name.strip().replace(' ', '_')


class TestBHiveOperation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        operation = BHiveOperation('myOp')
        assert operation.name == 'myOp'
        assert not operation.precondition

    def test_get_operation_name_from_scenario(self):
        scenario_mock = Mock()
        scenario_mock.name = 'Start Elevator'
        assert BHiveOperation.get_operation_name_from_scenario(scenario_mock) == 'Start_Elevator'
        scenario_mock.name = '   StopEscalator'
        assert BHiveOperation.get_operation_name_from_scenario(scenario_mock) == 'StopEscalator'


if __name__ == '__main__':
    unittest.main()

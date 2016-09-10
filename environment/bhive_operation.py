"""

"""
import unittest

from mock import Mock


class BHiveOperation(object):
    class Precondition(object):
        def __init__(self, expression):
            self.expression = expression

        def __str__(self):
            return ''.join(['PRE ', self.expression])

    class Assignment(object):
        def __init__(self, expression):
            self.expression = expression

        def __str__(self):
            return ''.join(['THEN ', self.expression])

    class OperationParameter(object):
        def __init__(self, name, type):
            self.name = name
            self.type = type

        @staticmethod
        def format_parameters_list(parameters_list):
            return '' if len(parameters_list) == 0 else ('(' + ','.join([p.name for p in parameters_list]) + ')')

    def __init__(self, name):
        self.name = name
        self.precondition = None
        self.assignment = None
        self.parameters_list = []

    def __str__(self):
        build_string = ' '.join(
            [self.name, BHiveOperation.OperationParameter.format_parameters_list(self.parameters_list)])
        build_string += '='
        build_string += '\nPRE ' + str(self.precondition)
        build_string += '\nTHEN ' + str(self.assignment)
        build_string += '\nEND'
        return build_string

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

    def test_formatting_operation_parameter_string(self):
        assert BHiveOperation.OperationParameter.format_parameters_list([]) == ''
        assert BHiveOperation.OperationParameter.format_parameters_list(
            [BHiveOperation.OperationParameter('a', 'A'),
             BHiveOperation.OperationParameter('b', 'B')]) == '(a,b)'


if __name__ == '__main__':
    unittest.main()

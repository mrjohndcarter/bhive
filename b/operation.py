"""

"""

import unittest

from mock import Mock

from bhive.utilities.scenario import get_normalized_scenario_name

class Operation(object):
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

        @staticmethod
        def format_parameters_list_as_precondition(parameters_list):
            return '' if len(parameters_list) == 0 else ' & '.join([(p.name + ' : ' + p.type) for p in parameters_list])

    def __init__(self, name):
        self.name = name
        self.state = None
        self.parameters_list = []
        self.test_predicates = []

    def __str__(self):
        build_string = ''.join(
            [self.name, Operation.OperationParameter.format_parameters_list(self.parameters_list)])
        build_string += ' = '
        build_string += '\nPRE ' + (
            Operation.OperationParameter.format_parameters_list_as_precondition(self.parameters_list) + ' ' if len(
                self.parameters_list) > 0 else '') + str(self.state.get_precondition())
        build_string += '\nTHEN ' + str(self.state.get_assignment())
        build_string += '\nEND'
        return build_string

    def add_parameter(self, parameter):
        # TODO check for duplicates?
        self.parameters_list.append(parameter)

    def add_test_assertion(self, test_assertion):
        self.test_predicates.append(test_assertion)

    def synthesize_test_predicate(self):
        return ' & '.join([str(p) for p in self.test_predicates])

    @staticmethod
    def get_operation_name_from_scenario(scenario):
        return get_normalized_scenario_name(scenario.name).replace(' ', '_')


class TestBHiveOperation(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        operation = Operation('myOp')
        assert operation.name == 'myOp'
        assert not operation.state

    def test_get_operation_name_from_scenario(self):
        scenario_mock = Mock()
        scenario_mock.name = 'Start Elevator'
        assert Operation.get_operation_name_from_scenario(scenario_mock) == 'Start_Elevator'
        scenario_mock.name = '   StopEscalator'
        assert Operation.get_operation_name_from_scenario(scenario_mock) == 'StopEscalator'

    def test_formatting_operation_parameter_string(self):
        assert Operation.OperationParameter.format_parameters_list([]) == ''
        assert Operation.OperationParameter.format_parameters_list(
            [Operation.OperationParameter('a', 'A'),
             Operation.OperationParameter('b', 'B')]) == '(a,b)'

    def test_precondition_parameter_string(self):
        assert Operation.OperationParameter.format_parameters_list_as_precondition([]) == ''
        assert Operation.OperationParameter.format_parameters_list_as_precondition(
            [Operation.OperationParameter('a', 'A')]) == 'a : A'
        assert Operation.OperationParameter.format_parameters_list_as_precondition(
            [Operation.OperationParameter('a', 'A'),
             Operation.OperationParameter('b', 'B')]) == 'a : A & b : B'

if __name__ == '__main__':
    unittest.main()

"""
Container for a B-Machine
"""
import os


# TODO: Don't support machine parameters
class Machine(object):
    class Parameter(object):
        def __init__(self, name):
            self.name = name
            self.type = None
            self.constraint_expression = None

        def param_type(self):
            return ' : '.join([self.name, self.type])

        def constraint(self):
            return self.constraint_expression

    class Set(object):
        def __init__(self, name):
            self.name = name
            self.enumeration = None

        def set(self):
            if not self.enumeration:
                return self.name
            else:
                return ' '.join([self.name, '=', self.enumeration])

    class Assignable(object):
        def __init__(self, name):
            self.name = name
            self.type = None
            self.assignment_expression = None

    class Constant(Assignable):
        def __init__(self, name):
            super(Machine.Constant, self).__init__(name)

        def property(self):
            return ' '.join([self.name, ':', self.type, '&', self.assignment_expression])

    class Variable(Assignable):
        def __init__(self, name):
            super(Machine.Variable, self).__init__(name)

        def invariant(self):
            return ' '.join([self.name, ':', self.type])

        def initialisation(self):
            return ' '.join([self.name, ':=', self.assignment_expression])

    MACHINE_EXTENSION = 'mch'
    WHITE_SPACE_SEP_STRING = '\t\t\t\t'
    LINE_SEP_STRING = '\n\n'

    def __init__(self, name):
        self.name = name
        self.operations = {}
        self.constants = {}
        self.variables = {}
        self.sets = {}
        self.parameters = []

    def __str__(self):
        build_string = self.WHITE_SPACE_SEP_STRING.join(['MACHINE', self.name])

        if len(self.parameters) > 0:
            build_string += ''.join(['(', ', '.join([p.name for p in self.parameters]), ')'])
            build_string += self.LINE_SEP_STRING
            build_string += 'CONSTRAINTS'
            build_string += self.WHITE_SPACE_SEP_STRING + ' & '.join(
                [(' & '.join([c.param_type() for c in self.parameters])),
                 (' & '.join([c.constraint_expression for c in self.parameters]))])

        build_string += self.LINE_SEP_STRING
        build_string += 'SETS'
        build_string += self.WHITE_SPACE_SEP_STRING + '; '.join([s.set() for s in self.sets.values()])
        build_string += self.LINE_SEP_STRING
        build_string += 'CONSTANTS'
        build_string += self.WHITE_SPACE_SEP_STRING + ' & '.join([c.name for c in self.constants.values()])
        build_string += self.LINE_SEP_STRING
        build_string += 'PROPERTIES'
        build_string += self.WHITE_SPACE_SEP_STRING + ' & '.join([c.property() for c in self.constants.values()])
        build_string += self.LINE_SEP_STRING
        build_string += 'VARIABLES'
        build_string += self.WHITE_SPACE_SEP_STRING + ', '.join([v.name for v in self.variables.values()])
        build_string += self.LINE_SEP_STRING
        build_string += 'INVARIANT'
        build_string += self.WHITE_SPACE_SEP_STRING + ' & '.join([v.invariant() for v in self.variables.values()])
        build_string += self.LINE_SEP_STRING
        build_string += 'INITIALISATION'
        build_string += self.WHITE_SPACE_SEP_STRING + ' || '.join([v.initialisation() for v in self.variables.values()])
        build_string += self.LINE_SEP_STRING

        build_string += 'OPERATIONS'
        build_string += self.LINE_SEP_STRING
        build_string += (';' + self.WHITE_SPACE_SEP_STRING).join([str(op) for op in self.operations.values()])

        build_string += '\nEND'
        return build_string

    def add_parameter(self, parameter):
        # TODO check for same name
        self.parameters.append(parameter)

    def add_set(self, set):
        self.sets[set.name] = set

    def add_variable(self, variable):
        self.variables[variable.name] = variable

    def add_constant(self, constant):
        self.constants[constant.name] = constant

    def add_operation(self, operation):
        self.operations[operation.name] = operation

    def get_operation_by_name(self, operation_name):
        return self.operations[operation_name]

    def get_filename(self, output_dir_name):
        return os.path.join(output_dir_name, '.'.join((self.name, self.MACHINE_EXTENSION)))

    # UNTESTED
    def synthesize(self):
        output_file = open(self.get_filename("output"), "w")
        output_file.write(str(self))
        output_file.close()

    @staticmethod
    def get_machine_name_from_feature_filename(path_to_feature):
        """
        returns machine name from feature path

        machine is features/MACHINENAME/featurefile.feature
        """
        path = os.path.dirname(path_to_feature)
        if not path:
            raise NameError
        return os.path.basename(os.path.normpath(path))


import unittest
from mock import Mock


class TestBHiveMachine(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_creation(self):
        machine = Machine('Elevator')
        assert machine.name == 'Elevator'

    def test_add_get_operation(self):
        machine = Machine('Elevator')
        operation = Mock(spec='_name')
        operation.name = "OpenDoor"
        machine.add_operation(operation)
        assert len(machine.operations) == 1
        assert machine.get_operation_by_name('OpenDoor') == operation

    def test_get_machine_name_from_feature_filename(self):
        assert Machine.get_machine_name_from_feature_filename(
            'features/MACHINENAME/featurefile.feature') == 'MACHINENAME'
        assert Machine.get_machine_name_from_feature_filename('BOB/name.feature') == 'BOB'
        self.assertRaises(NameError, Machine.get_machine_name_from_feature_filename, 'name.feature')


if __name__ == '__main__':
    unittest.main()

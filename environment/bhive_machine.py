"""
Container for a B-Machine
"""
import os


class BHiveMachine(object):
    MACHINE_EXTENSION = "mch"

    def __init__(self, name):
        self.name = name
        self.operations = {}

    def __str__(self):
        build_string = "Machine: "
        build_string += self.name
        build_string += "\n"
        for operation in self.operations.values():
            build_string += "\n" + str(operation)
        return build_string

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
        machine = BHiveMachine('Elevator')
        assert machine.name == 'Elevator'

    def test_add_get_operation(self):
        machine = BHiveMachine('Elevator')
        operation = Mock(spec='_name')
        operation.name = "OpenDoor"
        machine.add_operation(operation)
        assert len(machine.operations) == 1
        assert machine.get_operation_by_name('OpenDoor') == operation

    def test_get_machine_name_from_feature_filename(self):
        assert BHiveMachine.get_machine_name_from_feature_filename(
            'features/MACHINENAME/featurefile.feature') == 'MACHINENAME'
        assert BHiveMachine.get_machine_name_from_feature_filename('BOB/name.feature') == 'BOB'
        self.assertRaises(NameError, BHiveMachine.get_machine_name_from_feature_filename, 'name.feature')


if __name__ == '__main__':
    unittest.main()

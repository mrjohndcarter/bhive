"""
Bucket attached to behave context that holds all internal structures.
"""
import bhive.environment
import bhive.integration


class BHiveContext(object):
    def __init__(self):
        self.machines = {}
        self.typing = bhive.environment.typing.Typing()

    def register_machine(self, machine):
        bhive.integration.log_info('registered machine: {}'.format(machine.name))
        # TODO: does this need to be union'ed?
        self.machines[machine.name] = machine

    def get_machine_by_name(self, machine_name):
        return self.machines[machine_name]

    def synthesize(self):
        self.typing.synthesize()
        for machine in self.machines.values():
            machine.synthesize()

    def declare_set(self, type_name, parse_function=(lambda x: x), enumeration=None):
        self.typing.register_type(type_name, parse_function)
        self.typing.register_enumeration_for_type(type_name, enumeration)

import unittest

from mock import Mock


class TestBHiveContext(unittest.TestCase):
    def setUp(self):
        self.machine = Mock(name='TestMachine')
        self.behive_context = Mock(spec=['log_info'])
        self.context = BHiveContext(self.behive_context)

    def tearDown(self):
        pass

    def test_creation(self):
        assert len(self.context.machines) == 0

    def test_register_machine(self):
        self.context.register_machine(self.machine)
        assert len(self.context.machines) == 1

    def test_get_machine(self):
        self.context.register_machine(self.machine)
        assert self.context.get_machine_by_name(self.machine.name) == self.machine


if __name__ == '__main__':
    unittest.main()

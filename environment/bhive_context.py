"""
Bucket attached to behave context that holds all internal structures.
"""


class BHiveContext(object):
    def __init__(self, context):
        self.machines = {}
        self.behave_context = context

    def register_machine(self, machine):
        self.behave_context.log_info('Registered Machine: {}'.format(machine))
        self.machines[machine.name] = machine

    def get_machine_by_name(self, machine_name):
        return self.machines[machine_name]

    def synthesize(self):
        for machine in self.machines.values():
            machine.synthesize()


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

"""
Represents the constraints, invariants and state of a B Machine.
"""

# TODO create a context from the as a statement in a feature file.

class BContext(object):
    """
    The data and typing elements for a B Machine.
    """

    def __init__(self, name):
        self.name = name
        self.sets = {}

    def __str__(self):
        set_string = ''
        for (set_name, b_set) in self.sets.items():
            set_string += set_name + ':' + b_set + '\n'
        # TODO add initialisation
        # TODO add invariant
        # TODO add variables
        return 'BContext: ' + self.name + set_string

    def add_initialisation(self, name, initialisation):
        """
        Adds initialization for the variable name.
        """
        pass

    def add_invariant(self, invariant):
        """
        Adds a clause to the invariant.

        Unions with existing invariant.
        """
        pass

    def add_set(self, name, b_set):
        """
        Defines a set with name.
        """
        self.sets[name] = b_set

    def define_variable(self, name):
        """
        Defines a variable.

        Initialized using add_initialisation.
        Typed using add_invariant.
        """
        pass

    def get_set(self, name):
        """
        Gets a set by name.
        """
        return self.sets[name]

# self tests

import unittest

from bset import BSet

class TestBContext(unittest.TestCase):
    """
    TestBContext

    Tests BContext.
    """

    def setUp(self):
        self.test_context = BContext('test1')
        self.digit_set = BSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    def test_creation(self):
        """
        Tests context creation.
        """
        test_context = BContext('context')
        assert test_context.name == 'context'
        assert self.test_context.name == 'test1'

    def test_add_get_set(self):
        """
        Tests adding a set to a context.
        """
        self.test_context.add_set('digits', self.digit_set)
        assert self.test_context.get_set('digits') == BSet([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

    if __name__ == '__main__':
        unittest.main()

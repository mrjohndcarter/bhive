"""
Top level construction for a bhive system and helper functions.
"""

from behave import register_type

from ..typing import bcontext
from ..typing import bset
from ..typing import bfunction

from ..synthesis import synthesis

# Note:
#
# For arguments we always use 'context' for behave context.
#


class BEnvironment(object):

    """
    Top level bhive object.

    Collects contexts for all machines.
    """

    def __init__(self):
        self.machines = {}

    def add_context(self, machine_name, machine_context):
        """
        Adds a context to the environment.
        """
        self.machines[machine_name] = machine_context

    def get_context(self, machine_name):
        """
        Accessor for a context from the environment.
        """
        self.machines[machine_name]


def register_b_types(context):
    """
    Registers all the 'atomic' B types (Set, Function)
    """
    # register set
    register_type(Set=bset.BSet.parse_from_string)

    # register NAT
    # register NAT1
    # register relation
    # register sequence


def initialize_bhive(context):
    """
    Does everything that needs to happen after behave.

    Should be first call from behave's before_all
    """
    initialize_behive_environment(context)
    register_b_types(context)


def initialize_behive_environment(context):
    """
    Creates an empty context and attaches it to behave's context object.
    """
    context.bhive_environment = BEnvironment()


def finalize_bhive(context):
    """
    Does everything that happens for bhive after a behave invocation.
    """
    synthesis.synthesize(context)


# self tests

import unittest


class TestBEnvironment(unittest.TestCase):

    """
    TestBEnvironment

    Tests BEnvironment setup
    """

    def test_creation(self):
        """
        Tests environment setup.
        """
        pass

    if __name__ == '__main__':
        unittest.main()


# these define parse functions for types

#
# def parse_number(text):
#     return int(text)
#
#
# def parse_set(text):
#     return text
#
#
# def parse_enumeration(text):
#     return text
#
#
# def parse_element(text):
#     return text
#
#
# def parse_function(text):
#     return text
#
# # these register types
# # TODO : come up with a set of 'atomics' -- Set, Function, Element,
# # Domain, Range ??
# register_type(Number=parse_number)
# register_type(Set=parse_set)
# register_type(Enumeration=parse_enumeration)
# register_type(Element=parse_element)
# register_type(Function=parse_function)
#
# # setup / teardown stuff
#
#
# def before_scenario(context, scenario):
#     context.SUT = SUT()
#
#     # TODO : need a way to define these easier, and then have environment
#     # bring them in
#     context.SUT.sets.define_set_from_enumeration('soda', 'orange,coke,7up')
#     context.SUT.sets.define_set_from_enumeration('prices', '75,55,19')
#     context.SUT.sets.define_set_from_enumeration(
#         'baby_name',
#         'puppy,kid,kitten,foal')
#     context.SUT.sets.define_set_from_enumeration(
#         'animal_name',
#         'dog,goat,cat,horse')
#     context.SUT.sets.define_set_from_enumeration(
#         'domain_name',
#         'localhost,gateway,google-dns')
#     context.SUT.sets.define_set_from_enumeration(
#         'ip',
#         '127.0.0.1,192.168.1.1,8.8.8.8')
#     context.SUT.sets.define_set_from_enumeration(
#         'names',
#         'Alice,Bob,Carol,Dave,empty')
#     context.SUT.sets.define_set_from_enumeration('rooms', '1,2,3,penthouse')
#
#     # TODO : need a way to define these easier, and then have environment bring them in
#     # TODO : these don't have a property yet
#     context.SUT.functions.define_function('pricing', 'soda', 'prices')
#     context.SUT.functions.define_function('guests', 'rooms', 'names')
#
#     # TODO : need a way to initialize functions
#     context.SUT.functions.map('guests', '1', 'empty')
#     context.SUT.functions.map('guests', '2', 'empty')
#     context.SUT.functions.map('guests', '3', 'empty')
#     context.SUT.functions.map('guests', 'penthouse', 'empty')

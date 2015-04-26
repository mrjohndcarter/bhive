"""
Top level construction for a bhive system and helper functions.
"""

import logging

from functools import partial

from behave import register_type

#from ..synthesis import synthesis

#from ..typing import bcontext
from ..typing import bset
from ..typing import brelation

BHIVE_LOGGING_FORMAT = '%(asctime)-15s %(feature)s %(scenario)s %(step)s %(message)s'
BHIVE_LOGGING_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'


class BHiveIntegration(object):

    """
    Collects environmental hooks for bhive.

    Should you need to implement these in behave, you *must* call the respective
    bhive method.
    """

    # The following are behave-specific environment hooks
    # Run before/after each step:

    @staticmethod
    def before_step(context, step):
        """
        Run before each step.  Should be called from behave's before_step.
        """
        pass

    @staticmethod
    def after_step(context, step):
        """
        Run after each step.  Should be called from behave's after_step.
        """
        pass

    @staticmethod
    def before_scenario(context, scenario):
        """
        Run before each scenario.  Should be called from behave's before_scenario.
        """
        pass

    @staticmethod
    def after_scenario(context, scenario):
        """
        Run after each scenario.  Should be called from behave's after_scenario.
        """
        pass

    @staticmethod
    def before_feature(context, feature):
        """
        Run before each feature file.  Should be called from behave's before_feature.
        """
        pass

    @staticmethod
    def after_feature(context, feature):
        """
        Run after each feature file.  Should be called from behave's after_feature.
        """
        pass

    @staticmethod
    def before_tag(context, tag):
        """
        Run before each tag.  Should be called from behave's before_tag.
        """
        pass

    @staticmethod
    def after_tag(context, tag):
        """
        Run after each tag.  Should be called from behave's after_tag.
        """
        pass

    @staticmethod
    def before_all(context):
        """
        Run before behave.  Should be called from behave's before_all.
        """
        BHiveLogging.configure_logging(context)
        context.log_info('Initialized logging.')

        BHiveTyping.register_b_types(context)
        context.log_info('Registered B types.')

        # TODO: setup environment

    @staticmethod
    def after_all(context):
        """
        Run after bhave.  Should be called from behave's after_all.
        """
        # TODO: synthesize

        context.log_info('BHive completed.')
        pass


class BHiveLogging(object):

    """
    Provides a namespace for logging related functions.
    """

    @staticmethod
    def configure_logging(context):
        """
        Sets up logging mechanisms for bhive.

        Creates a logger, assigns logging level, creates a console handler and
        sets formatting.
        """
        # create logger
        context.logger = logging.getLogger('bhive')

        # set logging level
        context.logger.setLevel(logging.DEBUG)

        # set up a console handler
        context.logging_handler = logging.StreamHandler()
        context.logging_handler.setLevel(logging.DEBUG)

        # set formatting
        context.logging_formatter = logging.Formatter(
            BHIVE_LOGGING_FORMAT,
            datefmt=BHIVE_LOGGING_DATE_FORMAT)
        context.logging_handler.setFormatter(context.logging_formatter)

        # add handler
        context.logger.addHandler(context.logging_handler)

        # bind log levels into various functions
        context.log_critical = partial(BHiveLogging.log, context.logger, logging.CRITICAL)
        context.log_debug = partial(BHiveLogging.log, context.logger, logging.DEBUG)
        context.log_error = partial(BHiveLogging.log, context.logger, logging.ERROR)
        context.log_info = partial(BHiveLogging.log, context.logger, logging.INFO)
        context.log_warning = partial(BHiveLogging.log, context.logger, logging.WARNING)

    @staticmethod
    def log(logger, log_level, message, bhive_extra=None):

        if not bhive_extra:
            # if the behive details weren't specified, just fill in an empty object
            logger.log(log_level, message, extra={
                'feature': '',
                'scenario': '',
                'step': ''})
        else:
            logger.log(log_level, message, extra=bhive_extra)


class BHiveTyping(object):

    @staticmethod
    def register_b_types(context):
        """
        Registers all the 'atomic' B types (Set, Function)
        """
        # register set
        register_type(Set=bset.BSet.parse_from_string)

        # register NAT
        # register NAT1
        # register relation
        register_type(Relation=brelation.BRelation.parse_from_string)
        # register sequence

    @staticmethod
    def register_user_type(context, name, parse_function):
        pass

# class BEnvironment(object):
#
#     """
#     Top level bhive object.
#
#     Collects contexts for all machines.
#     """
#
#     def __init__(self, enable_output):
#         self.machines = {}
#         self.stdout = True
#         self.stderr = True
#         self.sets = {}
#
#     def add_context(self, machine_name, machine_context):
#         """
#         Adds a context to the environment.
#         """
#         self.machines[machine_name] = machine_context
#
#     def get_context(self, machine_name):
#         """
#         Accessor for a context from the environment.
#         """
#         self.machines[machine_name]

# def initialize_bhive(context, enable_output=True):
#     """
#     Does everything that needs to happen after behave.
#
#     Should be first call from behave's before_all
#     """
#     initialize_behive_environment(context, enable_output)
#     register_b_types(context)
#
#
# def initialize_behive_environment(context, enable_output):
#     """
#     Creates an empty context and attaches it to behave's context object.
#     """
#     #context.bhive_environment = BEnvironment(enable_output)
#
#
# def finalize_bhive(context):
#     """
#     Does everything that happens for bhive after a behave invocation.
#     """
#     synthesis.synthesize(context)


# How to use:
##
# Main should call initialize_bhive initially and finalize_bhive finally


# self tests

# import unittest
#
#
# class TestBEnvironment(unittest.TestCase):
#
#     """
#     TestBEnvironment
#
#     Tests BEnvironment setup
#     """
#
#     def test_creation(self):
#         """
#         Tests environment setup.
#         """
#         pass
#
#     if __name__ == '__main__':
#         unittest.main()


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

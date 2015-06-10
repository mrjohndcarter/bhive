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

# horizonal rule to help separate output
BHIVE_HR = '---------------------------------------------------------------'

# format string for log statements
BHIVE_LOGGING_FORMAT = '%(asctime)-15s %(feature)s %(scenario)s %(step)s %(message)s'

# how to format time in BHIVE_LOGGING_FORMAT
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
        context.log_debug('Before Step: %s' % step)

    @staticmethod
    def after_step(context, step):
        """
        Run after each step.  Should be called from behave's after_step.
        """
        context.log_debug('After Step: %s' % step)

    @staticmethod
    def before_scenario(context, scenario):
        """
        Run before each scenario.  Should be called from behave's before_scenario.
        """
        context.log_debug('Before Scenario: %s' % scenario)

    @staticmethod
    def after_scenario(context, scenario):
        """
        Run after each scenario.  Should be called from behave's after_scenario.
        """
        context.log_debug('After Scenario: %s' % scenario)

    @staticmethod
    def before_feature(context, feature):
        """
        Run before each feature file.  Should be called from behave's before_feature.
        """
        context.log_debug('Before Feature: %s' % feature)

    @staticmethod
    def after_feature(context, feature):
        """
        Run after each feature file.  Should be called from behave's after_feature.
        """
        context.log_debug('After Feature: %s' % feature)

    @staticmethod
    def before_tag(context, tag):
        """
        Run before each tag.  Should be called from behave's before_tag.
        """
        context.log_debug('Before Tag: %s' % tag)

    @staticmethod
    def after_tag(context, tag):
        """
        Run after each tag.  Should be called from behave's after_tag.
        """
        context.log_debug('After Tag: %s' % tag)

    @staticmethod
    def before_all(context):
        """
        Run before behave.  Should be called from behave's before_all.
        """
        print BHIVE_HR

        BHiveLogging.configure_logging(context)
        context.log_info('Initialized logging.')

        BHiveTyping.declare_b_types(context)
        context.log_info('Registered B types.')

        # TODO: setup environment

    @staticmethod
    def after_all(context):
        """
        Run after bhave.  Should be called from behave's after_all.
        """
        # TODO: synthesize

        context.log_info('BHive completed.')
        print BHIVE_HR


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
        context.log_critical = partial(
            BHiveLogging.log,
            context.logger,
            logging.CRITICAL)
        context.log_debug = partial(
            BHiveLogging.log,
            context.logger,
            logging.DEBUG)
        context.log_error = partial(
            BHiveLogging.log,
            context.logger,
            logging.ERROR)
        context.log_info = partial(
            BHiveLogging.log,
            context.logger,
            logging.INFO)
        context.log_warning = partial(
            BHiveLogging.log,
            context.logger,
            logging.WARNING)

    @staticmethod
    def log(logger, log_level, message, bhive_extra=None):
        """
        Helper log method.

        Used to curry various logging methods in configure_logging.
        Not meant to be called directly.
        """

        if not bhive_extra:
            # if the behive details weren't specified, just fill in an empty
            # object
            logger.log(log_level, message, extra={
                'feature': '',
                'scenario': '',
                'step': ''})
        else:
            logger.log(log_level, message, extra=bhive_extra)


class BHiveTyping(object):
    """
    Namespace for all BHive related typing mechanisms.
    """
    @staticmethod
    def register_user_type(context, name, parse_function):
        """
        Registers a user-defined bhive type (and registers it with behave).
        """
        # build a dict, pass it as kwargs
        # register type just takes TypeName=Function as its arguments
        # and adds to its internal dict of types
        register_type(**{name: parse_function})

        #print context
        #context.define_type(name)

        context.log_debug('Registered type: %s' % (name))

    @staticmethod
    def define_user_variable(context, name, type, enumeration):
        # TODO: variable name
        # TODO: invariant (typing on variable)
        # TODO: initialisation
        pass

    @staticmethod
    def define_user_constant(context, name):
        # TODO: define constant
        # TODO: do we need type or value?
        pass

    @staticmethod
    def define_user_set(context, name, enumeration=None):
        # TODO: define set
        # TODO: parse enumeration
        # TODO: if enumeration not defined, then add elements like:
        #   name1, name2, name3, etc.
        # what do these look like in a .feature?
        pass

    # TODO: what do with properties?
    # TODO: what to do with constraints?


    @staticmethod
    def declare_b_types(context):
        """
        Registers all the 'atomic' B types (Set, Function)

        Not meant to be called directly.
        """
        # register set
        # register_type(Set=bset.BSet.parse_from_string)

        BHiveTyping.register_user_type(
            context,
            'Set',
            bset.BSet.parse_from_string)

        # register NAT
        # register NAT1
        # register relation
        # register_type(Relation=brelation.BRelation.parse_from_string)

        BHiveTyping.register_user_type(
            context,
            'Relation',
            brelation.BRelation.parse_from_string)

        # register sequence

        # register_type(Foo=brelation.BRelation.parse_from_string)

class BHiveAddressSpace(object):
    """
    This is the 'per machine' storage mechanism.
    """

    def __init__(self, identifier):
        self.identifier = identifier
        self.variables = {}
        self.variable_invariants = {}

    def define(self, name, typing_invariant, rhs=None):
        """
        defines a variable in this address space

        rhs value not required.

        Note: this typing_invariant will be unioned with the machine invariant.
        """
        self.variables[name] = rhs
        self.variable_invariants[name] = typing_invariant

    def get(self, name):
        """
        returns a value with 'name' in this address space
        """
        return self.variables[name]

    def set(self, name, rhs):
        """
        sets a value with name to rhs value.
        """
        self.variables[name] = rhs

# TODO : self tests

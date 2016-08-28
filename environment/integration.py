from bhive.environment.environment import BHIVE_HR
from bhive.environment.typing import BHiveTyping
from bhive.environment.bhive_logging import BHiveLogging


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
        BHiveLogging.log()
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
        BHiveLogging.configure_logging(context)
        context.log_info('Initialized logging.')

        BHiveTyping.declare_b_types(context)
        context.log_info('Registered B types.')

    @staticmethod
    def after_all(context):
        """
        Run after bhave.  Should be called from behave's after_all.
        """
        context.log_info('BHive completed.')

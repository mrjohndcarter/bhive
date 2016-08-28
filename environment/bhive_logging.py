import logging

from functools import partial

# horizonal rule to help separate output
BHIVE_HR = '---------------------------------------------------------------'

# format string for log statements
BHIVE_LOGGING_FORMAT = '%(asctime)-15s %(feature)s %(scenario)s %(step)s %(message)s'

# how to format time in BHIVE_LOGGING_FORMAT
BHIVE_LOGGING_DATE_FORMAT = '%m/%d/%Y %I:%M:%S %p'

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
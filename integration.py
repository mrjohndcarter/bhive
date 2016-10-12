from b import machine, operation
from environment import bhive_context, state
from utilities import bhive_logging
from utilities.parse_functions import parse_bool, parse_integer, parse_nat, parse_nat1


class BHive_Internals(object):
    def __init__(self):
        self._context = bhive_context.BHiveContext()
        bhive_logging.BHiveLogging.configure_logging(self)

    def get_context(self):
        return self._context

    context = property(get_context)


instance = BHive_Internals()


def log_critical(s, extra={}):
    instance.log_critical(s, extra)


def log_debug(s, extra={}):
    instance.log_debug(s, extra)


def log_error(s, extra={}):
    instance.log_error(s, extra)


def log_info(s, extra={}):
    instance.log_info(s, extra)


def log_warning(s, extra={}):
    instance.log_warning(s, extra)


def before_all(context):
    # configure logging
    log_info("before_all")
    # register b types
    log_info("registering b-types")
    instance.context.declare_system_type('BOOL', parse_bool)
    instance.context.declare_system_type('INT', parse_integer)
    instance.context.declare_system_type('NAT', parse_nat)
    instance.context.declare_system_type('NAT1', parse_nat1)

def after_all(context):
    log_info('after_all')
    log_info('synthesizing')
    instance.context.synthesize()


def before_feature(context, feature):
    log_info('before_feature: {}'.format(feature.name))
    new_machine_name = machine.Machine.get_machine_name_from_feature_filename(feature.filename)
    new_machine = machine.Machine(new_machine_name)

    # TODO: where to parse this from?
    parameter = machine.Machine.Parameter('max_ticket')
    parameter.type = 'NAT1'
    parameter.constraint_expression = 'max_ticket <= 10'
    new_machine.add_parameter(parameter)

    # register the machine for this feature
    instance.context.register_machine(new_machine)

def after_feature(context, feature):
    log_info('after_feature: {}'.format(feature.name))
    # TODO finalize typing

def before_scenario(context, scenario):
    """
    This is where we create the new operation.
    """
    log_info('before_scenario: {}'.format(scenario.name))

    # Step 1 -- We initialize a fresh state
    # TODO: How to copy in the rest of the machine state
    context.state = state.State()

    machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
    temp_machine = instance.context.get_machine_by_name(machine_name)

    operation_name = operation.Operation.get_operation_name_from_scenario(scenario)
    temp_operation = operation.Operation(operation_name)
    temp_machine.add_operation(temp_operation)

    # TODO: everything below here is faked and needs to be generalized
    # set = machine.Machine.Set('WICKET')
    # temp_machine.add_set(set)
    #
    # set = machine.Machine.Set('NOT_DEFERRED')
    # set.enumeration = '{a,b}'
    # temp_machine.add_set(set)
    #
    # constant = machine.Machine.Constant('closed_sentinel')
    # constant.type = 'NAT'
    # constant.assignment_expression = 'closed_sentinel = 0'
    # temp_machine.add_constant(constant)

    # machine.define_constant()
    # machine.define_variable()
    # machine.define_set()

    # variable = machine.Machine.Variable('next_ticket')
    # variable.type = 'NAT'
    # variable.assignment_expression = '1'
    # temp_machine.add_variable(variable)
    #
    # variable = machine.Machine.Variable('current')
    # variable.type = 'NAT'
    # variable.assignment_expression = '0'
    # temp_machine.add_variable(variable)
    #
    # variable = machine.Machine.Variable('serving')
    # variable.type = 'WICKET --> NAT'
    # variable.assignment_expression = 'WICKET * {closed_sentinel}'
    # temp_machine.add_variable(variable)

    # variable = machine.Machine.Variable('running')
    # variable.type = 'BOOL'
    # variable.assignment_expression = 'FALSE'
    # temp_machine.add_variable(variable)


def after_scenario(context, scenario):
    """
    This is where we attach the state changes to the operation.
    """
    log_info('after_scenario: {}'.format(scenario.name))

    machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
    temp_machine = instance.context.get_machine_by_name(machine_name)

    operation_name = operation.Operation.get_operation_name_from_scenario(context.scenario)
    temp_operation = temp_machine.get_operation_by_name(operation_name)

    temp_operation.state = context.state


def before_step(context, step):
    log_info('before_step: {}'.format(step.name))


def after_step(context, step):
    log_info('after_step: {}'.format(step.name))


def declare_variable(behave_context, name, b_type, initialisation):
    machine_name = machine.Machine.get_machine_name_from_feature_filename(behave_context.feature.filename)
    temp_machine = instance.context.get_machine_by_name(machine_name)
    variable = machine.Machine.Variable(name)
    variable.type = b_type
    variable.assignment_expression = initialisation
    temp_machine.add_variable(variable)


def get_machine_by_name(machine_name):
    return instance.context.get_machine_by_name(machine_name)
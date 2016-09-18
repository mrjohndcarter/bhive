from b import machine, operation
from environment import bhive_context
from utilities import bhive_logging


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
    log_info("declaring b-types")
    # TODO: register b types
    pass


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


def before_scenario(context, scenario):
    log_info('before_scenario: {}'.format(scenario.name))

    machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
    temp_machine = instance.context.get_machine_by_name(machine_name)

    set = machine.Machine.Set('WICKET')
    temp_machine.add_set(set)

    set = machine.Machine.Set('NOT_DEFERRED')
    set.enumeration = '{a,b}'
    temp_machine.add_set(set)

    constant = machine.Machine.Constant('closed_sentinel')
    constant.type = 'NAT'
    constant.assignment_expression = 'closed_sentinel = 0'
    temp_machine.add_constant(constant)

    variable = machine.Machine.Variable('next_ticket')
    variable.type = 'NAT'
    variable.assignment_expression = '1'
    temp_machine.add_variable(variable)

    variable = machine.Machine.Variable('current')
    variable.type = 'NAT'
    variable.assignment_expression = '0'
    temp_machine.add_variable(variable)

    variable = machine.Machine.Variable('serving')
    variable.type = 'WICKET --> NAT'
    variable.assignment_expression = 'WICKET * {closed_sentinel}'
    temp_machine.add_variable(variable)


def after_scenario(context, scenario):
    log_info('after_scenario: {}'.format(scenario.name))


def before_step(context, step):
    log_info('before_step: {}'.format(step.name))

    machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
    temp_machine = instance.context.get_machine_by_name(machine_name)

    operation_name = operation.Operation.get_operation_name_from_scenario(context.scenario)
    temp_operation = operation.Operation(operation_name)
    # operation.precondition = '(current + 1) < next_ticket & current <= max_ticket'
    # operation.assignment = 'serving(ww) := current + 1 || current := current + 1'

    # op = BHiveOperation.OperationParameter('ww','WICKET')
    # operation.add_parameter(op)
    temp_machine.add_operation(temp_operation)

    if step.step_type == 'given':
        temp_operation.precondition = step.text
        temp_machine.add_operation(temp_operation)
        # context.bhive.register_machine(machine)

    if step.step_type == 'when':
        temp_operation.precondition = step.text
        temp_machine.add_operation(temp_operation)
        # context.bhive.register_machine(machine)

    if step.step_type == 'then':
        pass


def after_step(context, step):
    log_info('after_step: {}'.format(step.name))

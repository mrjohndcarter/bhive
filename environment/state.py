from bhive.b import machine, operation
import bhive.integration

class State(object):
    class Assertion(object):
        def __init__(self):
            self.lhs = None
            self.rhs = None
            self.operation = None

        def __str__(self):
            return ' '.join([str(self.lhs), self.operation, str(self.rhs)])

    class Assignment(object):
        def __init__(self):
            self.lhs = None
            self.rhs = None
            self.operation = None

        def __str__(self):
            return ' '.join([self.lhs, self.operation, self.rhs])

    def __init__(self):
        self.state_dict = {}
        self.assertions = []
        self.assignments = []

    def ensure_that(self, lhs, operation, rhs):
        # TODO: check type on assignment??
        temp_assertion = State.Assertion()
        temp_assertion.lhs = lhs
        temp_assertion.operation = operation
        temp_assertion.rhs = rhs
        self.assertions.append(temp_assertion)

    def test_that_always(self, context, lhs, test_op, rhs):
        machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
        temp_machine = bhive.integration.get_machine_by_name(machine_name)

        temp_machine.add_invariant('{} {} {}'.format(lhs, test_op, rhs))

    def test_that(self, context, lhs, test_op, rhs):
        # get the scenario we're talking about
        # add the test predicates to that

        machine_name = machine.Machine.get_machine_name_from_feature_filename(context.feature.filename)
        temp_machine = bhive.integration.get_machine_by_name(machine_name)
        operation_name = operation.Operation.get_operation_name_from_scenario(context.scenario)

        temp_operation = temp_machine.get_operation_by_name(operation_name)

        temp_assertion = State.Assertion()
        temp_assertion.lhs = lhs
        temp_assertion.operation = test_op
        temp_assertion.rhs = rhs

        temp_operation.add_test_assertion(temp_assertion)


    def assign(self, list_of_tuples):
        # TODO: check type on assignment??
        for t in list_of_tuples:
            temp_assignment = State.Assignment()
            temp_assignment.lhs, temp_assignment.operation, temp_assignment.rhs = t
            self.assignments.append(temp_assignment)


    def get_precondition(self):
        return ' & '.join([str(s) for s in self.assertions])


    def get_assignment(self):
        return ' || '.join([str(a) for a in self.assignments])

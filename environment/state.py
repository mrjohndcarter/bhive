class State(object):
    class Assertion(object):
        def __init__(self):
            self.lhs = None
            self.rhs = None
            self.operation = None

        def __str__(self):
            return ' '.join([self.lhs, self.operation, self.rhs])

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

    def assert_that(self, lhs, operation, rhs):
        temp_assertion = State.Assertion()
        temp_assertion.lhs = lhs
        temp_assertion.operation = operation
        temp_assertion.rhs = rhs
        self.assertions.append(temp_assertion)

    def assign(self, list_of_tuples):
        for t in list_of_tuples:
            temp_assignment = State.Assignment()
            temp_assignment.lhs, temp_assignment.operation, temp_assignment.rhs = t
            self.assignments.append(temp_assignment)

    def get_precondition(self):
        return ' & '.join([str(s) for s in self.assertions])

    def get_assignment(self):
        return ' || '.join([str(a) for a in self.assignments])

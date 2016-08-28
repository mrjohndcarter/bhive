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


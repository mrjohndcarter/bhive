"""
SUT - System Under Test for Bhive Dev
"""

# for now, this is just a big monolithic object while I figure things out

class SETS(object):
    """
    Table of all Defined Sets
    """
    def __init__(self):
        self.sets = {}

    def get_set(self, set_name):
        """
        Returns the definition of the set 'set_name'
        """
        return self.sets[set_name]

    def get_set_cardinality(self, set_name):
        """
        Returns the cardinality of the set 'set_name'
        """
        return len(self.sets[set_name])

    def is_set_defined(self, set_name):
        """
        Is the set 'set_name' defined?
        """
        return set_name in self.sets

    def define_set_from_enumeration(self, set_name, set_definition):
        """
        Defines a set with the given name and comma separated enumeration.
        """
        self.sets[set_name] = set_definition.split(',')

    def set_contains(self, set_name, element):
        """
        Tests membership of element in set 'set_name'
        """
        return element in self.sets[set_name]

class FUNCTIONS(object):
    """
    Table of all defined functions
    """
    def __init__(self, sets):
        self.functions = {}
        self.maps = {}
        self.sets = sets

    def define_function(self, function_name, domain, range_):
        if self.sets.is_set_defined(domain) and self.sets.is_set_defined(range_):
            self.functions[function_name] = (domain, range_)
            self.maps[function_name] = {}
        else:
            raise TypeError

    def is_function_defined(self, function_name):
        return function_name in self.functions

    def domain(self, function_name):
        if self.is_function_defined(function_name):
            (d, _) = self.functions[function_name]
            return d
        else:
            raise KeyError

    def range(self, function_name):
        if self.is_function_defined(function_name):
            (_, r) = self.functions[function_name]
            return r
        else:
            raise KeyError

    def map(self, function_name, from_, to):
        if self.is_function_defined(function_name):
            self.maps[function_name][from_] = to;
        else:
            raise KeyError
        
    def function_return(self, function_name, from_):
        if self.is_function_defined(function_name):
            return self.maps[function_name][from_];
        else:
            raise KeyError


class SUT(object):
    """
    Used for testing POC.
    """
    def __init__(self):
        self.sets = SETS()
        self.functions = FUNCTIONS(self.sets)

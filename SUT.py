"""
SUT - System Under Test for Bhive Dev
"""

# for now, this is just a big monolithic object while I figure things out

class SUT(object):
    """
    Used for testing POC.
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

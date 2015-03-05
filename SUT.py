
class SUT(object):
    """
    Used for testing POC.
    """
    def __init__(self):
        self.sets = {}

    def get_set(self, set_name):
        return self.sets[set_name]

    def get_cardinality(self, set_name):
        return len(self.sets[set_name])

    def defined(self, set_name):
        return set_name in self.sets

    def define_set(self, set_name, set_definition):
        self.sets[set_name] = set_definition.split(',')

    def contains(self, set_name, element):
        return element in self.sets[set_name]

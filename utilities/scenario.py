import unittest


def get_normalized_scenario_name(scenario_name):
    # scenario outline names should be of the format "name -- @X.Y"
    # return everything before the -- sans whitespace
    return scenario_name.split('--')[0].strip()


class TestBHiveContext(unittest.TestCase):
    def test_get_scenario_name(self):
        assert get_normalized_scenario_name('operation -- @1.2') == 'operation'
        assert get_normalized_scenario_name('operation') == 'operation'


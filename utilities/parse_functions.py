
def parse_bool(s):
    if s == 'TRUE':
        return True
    elif s == 'FALSE':
        return False
    else:
        raise ValueError("Could not parse BOOL from: {}".format(s))


def parse_integer(s):
    return int(s)


def parse_nat(s):
    return int(s)


def parse_nat1(s):
    value = int(s)
    if value <= 0:
        raise ValueError("Negative value parsed from: {}".format(s))
    return value


import unittest


class TestBHiveContext(unittest.TestCase):
    def test_parse_bool(self):
        assert parse_bool('TRUE')
        assert not parse_bool('FALSE')
        self.assertRaises(ValueError, parse_bool,'')
        self.assertRaises(ValueError, parse_bool, 'blah...')

    def test_parse_integer(self):
        assert parse_integer('7') == 7
        assert parse_integer('-7') == -7
        self.assertRaises(ValueError, parse_integer, '')
        self.assertRaises(ValueError, parse_integer, 'abc')

    def test_nat(self):
        assert parse_nat('99') == 99
        assert parse_nat('0') == 0
        self.assertRaises(ValueError, parse_integer, 'boris')

    def test_nat1(self):
        assert parse_nat1('8') == 8
        self.assertRaises(ValueError, parse_nat1, '0')
        self.assertRaises(ValueError, parse_nat1, '-8')
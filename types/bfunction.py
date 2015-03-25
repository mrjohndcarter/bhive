"""
A function

A relationship between two sets.
"""

from bset import BSet

class BFunction(object):
    """
    Maps domain set to range set.
    """
    def __init__(self, func_domain, func_range):
        self.function_domain = func_domain
        self.function_range = func_range
        self.mapping = {}

    def __contains__(self, d):
        return d in self.mapping

    def __len__(self):
        return len(self.mapping)

    def __delitem__(self, d):
        del(self.mapping[d])

    def __getitem__(self, d):
        return self.mapping[d]

    def __setitem__(self, d, r):
        if d not in self.function_domain:
            raise KeyError
        if r not in self.function_range:
            raise ValueError
        self.mapping[d] = r

    def domain(self):
        return BSet(self.mapping.keys())

    def range(self):
        return BSet(self.mapping.values())

# self tests

import unittest


class TestBFunction(unittest.TestCase):

    """
    TestBFunction

    Tests BSet.
    """

    def setUp(self):
        # vowels
        self.vowels = BSet()
        self.vowels.add('a')
        self.vowels.add('e')
        self.vowels.add('i')
        self.vowels.add('o')
        self.vowels.add('u')

        # natural numbers <= 10
        self.nat10 = BSet([0,1,2,3,4,5,6,7,8,9,10])

        self.vowel_mapping = BFunction(self.vowels, self.nat10)
        self.vowel_mapping['a'] = 0
        self.vowel_mapping['e'] = 1
        self.vowel_mapping['i'] = 2
        self.vowel_mapping['o'] = 4
        self.vowel_mapping['u'] = 8

    def test_empty(self):
        """
        Test empty function.
        """
        vowel_mapping = BFunction(self.vowels, self.nat10)
        assert len(vowel_mapping) == 0

    def test_set(self):
        """
        Test mapping d -> r
        """
        vowel_mapping = BFunction(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2
        vowel_mapping['o'] = 4
        vowel_mapping['u'] = 8
        assert len(vowel_mapping) == 5

    def test_get(self):
        """
        Test getting r from a d.
        """
        vowel_mapping = BFunction(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2
        vowel_mapping['o'] = 4
        vowel_mapping['u'] = 8

        vowels = ['a','e','i','o','u']
        numbers = [0, 1, 2, 4, 8]

        for i in range(len(vowels)):
            assert vowel_mapping[vowels[i]] == numbers[i]

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'missing')

    def test_domain_range(self):
        """
        Test that we can't map values outside of domain/ranges.
        """
        vowel_mapping = BFunction(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'b')
        self.assertRaises(ValueError, vowel_mapping.__setitem__, 'a', 13)

        assert vowel_mapping['a'] == 0

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'o')

        assert len(vowel_mapping) == 3

    def test_delete(self):
        """
        Test deleting mappings.
        """
        vowels = ['a','e','i','o','u']

        for i in range(5):
            del self.vowel_mapping[vowels[i]]
            assert len(self.vowel_mapping) == (len(vowels) - i - 1)

    def test_domain(self):
        """
        Test getting domain of function.
        """
        assert self.vowel_mapping.domain() == BSet(['a','e','i','o','u'])
        del self.vowel_mapping['a']
        assert self.vowel_mapping.domain() == BSet(['e','i','o','u'])

    def test_range(self):
        """
        Test getting range of function.
        """
        assert self.vowel_mapping.range() == BSet([0,1,2,4,8])
        del self.vowel_mapping['a']
        assert self.vowel_mapping.range() == BSet([1,2,4,8])

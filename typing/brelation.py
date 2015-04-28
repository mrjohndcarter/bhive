"""
Relation

A relatioship between two Sets.
"""

from bhive.typing.bset import BSet

from collections import defaultdict

from itertools import chain

#TODO: Relation step library.

class BRelation(object):

    """
    Maps domain set to range set.
    """

    def partial_function(self):
        """
        Returns true if this relation is a partial function.

        Also used a key to represent the type of relation.
        """
        return False

    def total_function(self):
        """
        Returns true if this relation is a total function.

        Also used a key to represent the type of relation.
        """
        return False

    def partial_injection(self):
        """
        Returns true if this relation is a partial injection.

        Also used a key to represent the type of relation.
        """
        return False

    def total_injection(self):
        """
        Returns true if this relation is a total injection.

        Also used a key to represent the type of relation.
        """
        return False

    def partial_surjection(self):
        """
        Returns true if this relation is a partial surjection.

        Also used a key to represent the type of relation.
        """
        return False

    def total_surjection(self):
        """
        Returns true if this relation is a total surjection.

        Also used a key to represent the type of relation.
        """
        return False

    def total_bijection(self):
        """
        Returns true if this relation is a total bijection (injective, surjective)

        Also used a key to represent the type of relation.
        """
        return False

    # relation and function opertor symbols
    function_properties = {
        # maps function types to symbols:
        partial_function: {'symbol': '+->', 'description' : 'Partial Function'},
        total_function: {'symbol': '-->', 'description' :  'Total Function'},
        partial_injection: {'symbol': ' >+>', 'description' : 'Partial Injection'},
        total_injection: {'symbol': '>->', 'description' : 'Total Injection'},
        partial_surjection: {'symbol': ' +->>', 'description' : 'Partial Surjection'},
        total_surjection: {'symbol': ' -->>', 'description' : 'Total Surjection'},
        total_bijection: {'symbol': '>->>', 'description' : 'Total Bijection'},
    }

    function_operators = {
        '+->': partial_function,
        '-->': total_function,
        '>+>': partial_injection,
        '>->': total_injection,
        '+->>': partial_surjection,
        '-->>': total_surjection,
        '>->>': total_bijection
    }

    maplet = '|->'

    @staticmethod
    def split_maplet(maplet_string):
        """
        Utility method to split a string into 3 parts of maplet

        d (operator) r

        """
        split_array = maplet_string.strip().split(' ')
        return (split_array[0].strip(), split_array[1].strip(), split_array[2].strip())

    @staticmethod
    def parse_from_string(string):
        """
        Returns a BRelation as parsed from the comma separated maplets.

        E.g.:

        "(SET operator SET), a |-> b, a |-> d"

        """
        maplet_list = string.split(',')

        print maplet_list

        (domain_operand, relation_operator, range_operand) = BRelation.split_maplet(maplet_list.pop(0))

        if relation_operator not in BRelation.function_operators:
            raise SyntaxError

        new_relation = BRelation(domain_operand, range_operand, relation_operator)

        for current_maplet in maplet_list:
            (domain_operand, relation_operator, range_operand) = BRelation.split_maplet(current_maplet)

            if relation_operator != BRelation.maplet:
                print relation_operator
                raise SyntaxError

            new_relation[domain_operand] = range_operand

        # verify the rule applies

        return new_relation

    def __init__(
            self,
            relation_domain,
            relation_range,
            relation_rule=None):

        self.relation_domain = relation_domain
        self.relation_range = relation_range
        self.mapping = defaultdict(BSet)

        # a relation rule of None is just a general relation
        self.relation_rule = relation_rule

    def __contains__(self, domain_element):
        """
        Tests for a mapping of domain_element.
        """
        return domain_element in self.mapping

    def __len__(self):
        """
        Returns number of mappings in the function.
        """
        return len(self.mapping)

    def __str__(self):
        relation_symbol = '|->' if not self.relation_rule else self.relation_rule
        build_string = self.relation_domain + relation_rule + self.relation_range
        return build_string

    def __delitem__(self, domain_element):
        """
        Deletes a mapping from the function.
        """
        del self.mapping[domain_element]

    def __getitem__(self, domain_element):
        """
        Returns a BSet of Values mapped from d

        Raises KeyError if d not present
        """
        if domain_element not in self.mapping:
            raise KeyError

        return self.mapping[domain_element]

    def __setitem__(self, domain_element, range_element):
        """
        Creates a mapping from d -> r.
        """
        if domain_element not in self.relation_domain:
            raise KeyError
        if range_element not in self.relation_range:
            raise ValueError
        if domain_element in self.mapping:
            self.mapping[domain_element].add(range_element)
        else:
            self.mapping[domain_element] = BSet([range_element])

    def domain(self):
        """
        Returns domain of this function.
        """
        return BSet(self.mapping.keys())

    def range(self):
        """
        Returns range of this function.
        """
        return BSet(chain.from_iterable(self.mapping.values()))

    def domain_restriction(self, domain_set):
        """
        Returns all values in range for each value in domain_set

        b syntax: S <| domain_set
        """
        # TODO: optimize!
        built_range = BSet()
        for element in domain_set:
            # just skip missing keys
            if element in self.mapping:
                for value_list in self[element]:
                    built_range.add(value_list)
        return built_range

    def range_restriction(self, range_set):
        """
        Returns all values in domain mapped to values in range_set

        b syntax: S |> range_set
        """
        # TODO : optimize!
        built_domain = BSet()
        for (key, values) in self.mapping.items():
            for value in values:
                if value in range_set:
                    built_domain.add(key)
        return built_domain

    def is_function(self):
        """
        Is the relation a function?
        """

# self tests

import unittest


class TestBRelation(unittest.TestCase):
    """
    TestBRelation

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
        self.nat10 = BSet([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        self.vowel_mapping = BRelation(self.vowels, self.nat10)
        self.vowel_mapping['a'] = 0
        self.vowel_mapping['e'] = 1
        self.vowel_mapping['i'] = 2
        self.vowel_mapping['o'] = 4
        self.vowel_mapping['u'] = 8

        self.cars = BSet(['jetta', 'golf', 'cabriolet', 'passat'])
        self.people = BSet(['alice', 'bob', 'carol', 'david'])

        self.car_owners = BRelation(self.people, self.cars)

        self.car_owners['alice'] = 'jetta'
        self.car_owners['alice'] = 'passat'
        self.car_owners['bob'] = 'golf'

    def test_empty(self):
        """
        Test empty function.
        """
        vowel_mapping = BRelation(self.vowels, self.nat10)
        assert len(vowel_mapping) == 0

    def test_set(self):
        """
        Test mapping d -> r
        """
        vowel_mapping = BRelation(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2
        vowel_mapping['o'] = 4
        vowel_mapping['u'] = 8
        assert len(vowel_mapping) == 5

    def test_contains(self):
        """
        Test membership predicate.
        """
        assert 'alice' in self.car_owners
        assert 'bob' in self.car_owners

    def test_get(self):
        """
        Test getting r from a d.
        """
        vowel_mapping = BRelation(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2
        vowel_mapping['o'] = 4
        vowel_mapping['u'] = 8
        vowel_mapping['u'] = 3

        vowels = ['a', 'e', 'i', 'o', 'u']
        numbers = [BSet([0]), BSet([1]), BSet([2]), BSet([4]), BSet([3, 8])]

        for i in range(len(vowels)):
            assert vowel_mapping[vowels[i]] == numbers[i]

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'missing')

    def test_domain_range(self):
        """
        Test that we can't map values outside of domain/ranges.
        """
        vowel_mapping = BRelation(self.vowels, self.nat10)
        vowel_mapping['a'] = 0
        vowel_mapping['e'] = 1
        vowel_mapping['i'] = 2

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'b')
        self.assertRaises(ValueError, vowel_mapping.__setitem__, 'a', 13)

        assert vowel_mapping['a'] == BSet([0])

        self.assertRaises(KeyError, vowel_mapping.__getitem__, 'o')

        assert len(vowel_mapping) == 3

    def test_delete(self):
        """
        Test deleting mappings.
        """
        vowels = ['a', 'e', 'i', 'o', 'u']

        for i in range(5):
            del self.vowel_mapping[vowels[i]]
            assert len(self.vowel_mapping) == (len(vowels) - i - 1)

    def test_domain(self):
        """
        Test getting domain of function.
        """
        assert self.vowel_mapping.domain() == BSet(['a', 'e', 'i', 'o', 'u'])
        del self.vowel_mapping['a']
        assert self.vowel_mapping.domain() == BSet(['e', 'i', 'o', 'u'])

    def test_range(self):
        """
        Test getting range of function.
        """
        assert self.vowel_mapping.range() == BSet([0, 1, 2, 4, 8])
        del self.vowel_mapping['a']
        assert self.vowel_mapping.range() == BSet([1, 2, 4, 8])
        self.vowel_mapping['e'] = 6
        assert self.vowel_mapping.range() == BSet([1, 2, 4, 6, 8])

    def test_domain_restriction(self):
        """
        Tests getting values for a subset of the domain.
        """
        assert self.car_owners.domain_restriction(
            BSet(['alice'])) == BSet(['jetta', 'passat'])
        assert self.car_owners.domain_restriction(BSet(['david'])) == BSet([])

    def test_range_restriction(self):
        """
        Test getting domain elements for a subset of the range.
        """
        self.car_owners['bob'] = 'jetta'
        assert self.car_owners.range_restriction(
            BSet(['golf'])) == BSet(['bob'])
        assert self.car_owners.range_restriction(
            BSet(['jetta'])) == BSet(['alice', 'bob'])

    def test_parse_from_string(self):
        """
        Tests parsing a relation from a string of maplets.
        """
        dir(self)
        print BRelation.parse_from_string('NUM +-> LETTERS, a |-> b, c |-> d')

if __name__ == '__main__':
    unittest.main()

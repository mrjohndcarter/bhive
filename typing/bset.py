"""
A Set

Wraps python's mutable set.
"""
from itertools import product, chain, combinations


# TODO: Set step library.

class BSet(object):
    """
    Augments behavior provided by set

    Uses aggregation to implement a more functional set.
    """

    @staticmethod
    def parse_from_string(string):
        """
        Returns a BSet as parsed from the comma separated string.

        Note: We currently parse a set of strings.
        """
        element_list = []
        for an_element in string.split(','):
            element_list.append(an_element.strip())
        return BSet(element_list)

    def __init__(self, iterable=None):
        if iterable:
            self.value = set(iterable)
        else:
            self.value = set()

    def __contains__(self, item):
        return item in self.value

    def __hash__(self):
        # yeah -- it's weird
        # need to define a consistent hash so that we fall back to __eq__
        # default hash just uses id
        return 42

    def __eq__(self, iterable):
        sym_diff = BSet(self.value.symmetric_difference(iterable))
        return len(sym_diff) == 0

    def __iter__(self):
        return iter(self.value)

    def __len__(self):
        return len(self.value)

    def __lt__(self, iterable):
        return self.value.issubset(iterable)

    def __str__(self):
        return 'BSet: ' + str(self.value)

    def add(self, item):
        """
        Add items to set.
        """
        self.value.add(item)

    def clear(self):
        """
        Removes all elements from set.
        """
        self.value.clear()

    def discard(self, item):
        """
        Removes item from set (if present).
        """
        self.value.discard(item)

    def remove(self, item):
        """
        Removes item from set.

        raises KeyError if not present.
        """
        self.value.remove(item)

    # operations with other sets

    def issubset(self, iterable_t):
        """
        is the set a subset of iterable_t?

        b syntax: s <: iterable_t
        """
        return self.value.issubset(iterable_t)

    def isstrictsubset(self, iterable_t):
        """
        is the set a strict subset of iterable_t?

        b syntax: s <<: iterable_t
        """
        return self.value.issubset(iterable_t) and len(
            iterable_t) > len(self.value)

    def issuperset(self, iterable_t):
        """
        is iterable_t a super set of the set?
        """
        return self.value.issuperset(iterable_t)

    def union(self, iterable_t):
        """
        Returns union of set and iterable_t

        b syntax: s Union T
        """
        return BSet(self.value.union(iterable_t))

    def intersection(self, iterable_t):
        """
        Returns insection of set and iterable_t

        b syntax: s Inters T
        """
        return BSet(self.value.intersection(iterable_t))

    def difference(self, iterable_t):
        """
        Returns difference of set and iterable_t

        b syntax: s - t
        """
        return BSet(self.value.difference(iterable_t))

    def symmetric_difference(self, iterable_t):
        """
        Returns symmetric difference of set and iterable_t
        """
        return BSet(self.value.symmetric_difference(iterable_t))

    def cartestian_product(self, iterable_t):
        """
        Returns cartestian product of set and iterable_t

        Represented as a set of tuples.
        """
        return BSet(sorted(product(self.value, iterable_t)))

    def powerset(self):
        """
        Returns powerset of set.  Sorted as subsets.

        b syntax: pow(s)
        """
        tuples = chain.from_iterable(
            combinations(self.value, r) for r in range(len(self.value) + 1))
        return BSet(sorted([BSet(a) for a in tuples]))


# self tests

import unittest


class TestBSet(unittest.TestCase):
    """
    TestBSet

    Tests BSet.
    """

    def setUp(self):
        self.empty_set = BSet()
        self.abc_set = BSet()
        self.cde_set = BSet()

        self.abc_set.add('a')
        self.abc_set.add('b')
        self.abc_set.add('c')

        self.cde_set.add('c')
        self.cde_set.add('d')
        self.cde_set.add('e')

    def test_equality(self):
        """
        Test equality between two BSets
        """
        new_set_abc = BSet()
        new_set_abc.add('a')
        new_set_abc.add('b')
        new_set_abc.add('c')
        assert self.abc_set == new_set_abc

    def test_mixed_equality(self):
        """
        Test equality between a BSet and python set
        """
        python_set_abc = set(['a', 'b', 'c'])
        assert self.abc_set == python_set_abc

    def test_creation(self):
        """
        Tests creation of a new set.
        """
        new_set_a = BSet()

        assert self.empty_set != new_set_a
        assert str(self.empty_set) == str(new_set_a)
        assert len(new_set_a) == 0

    def test_creation_from_iterable(self):
        """
        Tests creation from an iterable.
        """
        new_set_abc = BSet(['a', 'b', 'c'])
        assert new_set_abc == self.abc_set

    def test_parse_from_string(self):
        """
        Tests creation of a set from a string.

        Note: This creates a set
        """
        assert BSet.parse_from_string('a, b, c') == self.abc_set

    def test_add(self):
        """
        Tests adding elements to a set.
        """
        new_set_a = BSet()

        new_set_a.add('a')
        new_set_a.add('b')
        new_set_a.add('c')
        new_set_a.add('a')

        assert self.empty_set != new_set_a
        assert len(new_set_a) == 3
        assert 'a' in new_set_a
        assert 'b' in new_set_a
        assert 'c' in new_set_a
        assert 'd' not in new_set_a

    def test_remove(self):
        """
        Tests remove elements from a set.
        """
        assert len(self.abc_set) == 3
        self.abc_set.remove('a')
        assert len(self.abc_set) == 2
        self.abc_set.remove('b')
        assert len(self.abc_set) == 1
        self.abc_set.remove('c')
        assert len(self.abc_set) == 0

        # test that trying to delete a missing element throws KeyError
        self.assertRaises(KeyError, self.abc_set.remove, 'd')

    def test_discard(self):
        """
        Test discarding elements from set (no exception thrown).
        """
        assert len(self.abc_set) == 3
        self.abc_set.discard('a')
        assert len(self.abc_set) == 2
        self.abc_set.discard('b')
        assert len(self.abc_set) == 1
        self.abc_set.discard('c')
        assert len(self.abc_set) == 0
        self.abc_set.discard('d')
        assert len(self.abc_set) == 0

    def test_clear(self):
        """
        Test clearing the set.
        """
        assert len(self.abc_set) == 3
        self.abc_set.clear()
        assert len(self.abc_set) == 0

    def test_subsets(self):
        """
        Test subset and superset operations.
        """
        ab_set = BSet()
        ab_set.add('a')
        ab_set.add('b')

        # ab_set <: ab_set
        assert ab_set.issubset(ab_set)
        assert ab_set < ab_set

        # ab_set <: abc_set
        assert ab_set.issubset(self.abc_set)
        assert ab_set < self.abc_set

        # is abc_set a superset of ab_set
        assert self.abc_set.issuperset(ab_set)

        # not ab_set is superset of abc_set
        assert not ab_set.issuperset(self.abc_set)

        # not abc_set <: ab_set
        assert not self.abc_set.issubset(ab_set)

        # not ab_set <<: ab_set
        assert not ab_set.isstrictsubset(ab_set)

        # ab_set <<: abc_set
        assert ab_set.isstrictsubset(self.abc_set)

        # empty set <: ab_set
        assert self.empty_set.issubset(ab_set)

        # empty set <<: ab_set
        assert self.empty_set.isstrictsubset(ab_set)

        # empty set <: empty set
        assert self.empty_set.issubset(self.empty_set)

        # not empty set <<: empty set
        assert not self.empty_set.isstrictsubset(self.empty_set)

    def test_union(self):
        """
        Tests union operation.
        """
        abcde_set = BSet(['a', 'b', 'c', 'd', 'e'])

        cde_set = BSet()
        cde_set.add('c')
        cde_set.add('d')
        cde_set.add('e')

        union_abcde_set = self.abc_set.union(cde_set)

        assert union_abcde_set == abcde_set

    def test_intersection(self):
        """
        Tests intersection operation.
        """
        assert self.abc_set.intersection(self.cde_set) == BSet(['c'])
        assert self.abc_set.intersection(self.empty_set) == BSet()

    def test_difference(self):
        """
        Tests set difference.
        """
        assert self.abc_set.difference(self.cde_set) == BSet(['a', 'b'])
        assert self.cde_set.difference(self.abc_set) == BSet(['d', 'e'])

    def test_symmetric_difference(self):
        """
        Tests symmetric difference.
        """
        assert self.abc_set.symmetric_difference(
            self.cde_set) == BSet(['a', 'b', 'd', 'e'])

    def test_cartestian(self):
        """
        Tests calculating cartesian projection of two sets.
        """
        cart_product_actual = BSet([])
        cart_product_actual.add(('a', 'c'))
        cart_product_actual.add(('a', 'd'))
        cart_product_actual.add(('a', 'e'))
        cart_product_actual.add(('b', 'c'))
        cart_product_actual.add(('b', 'd'))
        cart_product_actual.add(('b', 'e'))
        cart_product_actual.add(('c', 'c'))
        cart_product_actual.add(('c', 'd'))
        cart_product_actual.add(('c', 'e'))

        cart_product = self.abc_set.cartestian_product(self.cde_set)

        assert len(cart_product) == 9
        assert cart_product_actual == cart_product
        assert self.abc_set.cartestian_product(
            self.empty_set) == self.empty_set

    def test_powerset(self):
        """
        Tests calculating powerset of a set.
        """
        power_set_actual = BSet()
        power_set_actual.add(BSet())
        power_set_actual.add(BSet(['a']))
        power_set_actual.add(BSet(['b']))
        power_set_actual.add(BSet(['c']))
        power_set_actual.add(BSet(['a', 'b']))
        power_set_actual.add(BSet(['a', 'c']))
        power_set_actual.add(BSet(['b', 'c']))
        power_set_actual.add(BSet(['a', 'b', 'c']))

        power_set = self.abc_set.powerset()

        # number of subsets is 2^N where N is len(S)
        assert len(power_set) == 2 ** len(self.abc_set)
        assert power_set_actual == power_set

    def test_set_of_sets1(self):
        """
        Tests equality between two sets containing sets.
        """
        set_a = BSet()
        set_a.add(self.abc_set)

        set_b = BSet()
        set_b.add(self.abc_set)

        assert set_a == set_b


if __name__ == '__main__':
    unittest.main()

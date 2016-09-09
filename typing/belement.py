"""
An element in a Set.
"""


class BElement(object):
    """
    BElement

    A unique element in a Set.
    """

    def __init__(self, content):
        self.value = content

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        return hash(self.value)


# self tests

import unittest


class TestBElement(unittest.TestCase):
    """
    TestBElement

    Tests BElement.
    """

    def setUp(self):
        self.element_a = BElement('a')

    def test_creation(self):
        """
        Tests creation of an element.
        """
        new_element_a = BElement('a')
        assert str(self.element_a) == str(new_element_a)
        assert hash(self.element_a) == hash(new_element_a)
        assert self.element_a != new_element_a


if __name__ == '__main__':
    unittest.main()

"""
Provides synthesis of B Machines.
"""


class Synthesizable(object):
    """
    Abstract base class for all types that can be synthesized.
    """

    def sythesize(self):
        """
        Synthesizes the entire element.
        """
        raise NotImplementedError("Should have implemented this")

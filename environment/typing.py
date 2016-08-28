from behave import register_type

from bhive.typing import bset, brelation


class BHiveTyping(object):
    """
    Namespace for all BHive related typing mechanisms.
    """
    @staticmethod
    def register_user_type(context, name, parse_function):
        """
        Registers a user-defined bhive type (and registers it with behave).
        """
        # build a dict, pass it as kwargs
        # register type just takes TypeName=Function as its arguments
        # and adds to its internal dict of types
        register_type(**{name: parse_function})

        #print context
        #context.define_type(name)

        context.log_debug('Registered type: %s' % (name))

    @staticmethod
    def define_user_variable(context, name, type, enumeration):
        # TODO: variable name
        # TODO: invariant (typing on variable)
        # TODO: initialisation
        pass

    @staticmethod
    def define_user_constant(context, name):
        # TODO: define constant
        # TODO: do we need type or value?
        pass

    @staticmethod
    def define_user_set(context, name, enumeration=None):
        # TODO: define set
        # TODO: parse enumeration
        # TODO: if enumeration not defined, then add elements like:
        #   name1, name2, name3, etc.
        # what do these look like in a .feature?
        pass

    # TODO: what do with properties?
    # TODO: what to do with constraints?


    @staticmethod
    def declare_b_types(context):
        """
        Registers all the 'atomic' B types (Set, Function)

        Not meant to be called directly.
        """
        # register set
        # register_type(Set=bset.BSet.parse_from_string)

        BHiveTyping.register_user_type(
            context,
            'Set',
            bset.BSet.parse_from_string)

        # register NAT
        # register NAT1
        # register relation
        # register_type(Relation=brelation.BRelation.parse_from_string)

        BHiveTyping.register_user_type(
            context,
            'Relation',
            brelation.BRelation.parse_from_string)

        # register sequence

        # register_type(Foo=brelation.BRelation.parse_from_string)
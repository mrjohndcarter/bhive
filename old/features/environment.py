from SUT import SUT

from behave import register_type


# these define parse functions for types


def parse_number(text):
    return int(text)


def parse_set(text):
    return text


def parse_enumeration(text):
    return text


def parse_element(text):
    return text


def parse_function(text):
    return text


# these register types
# TODO : come up with a set of 'atomics' -- Set, Function, Element,
# Domain, Range ??
register_type(Number=parse_number)
register_type(Set=parse_set)
register_type(Enumeration=parse_enumeration)
register_type(Element=parse_element)
register_type(Function=parse_function)


# setup / teardown stuff


def before_scenario(context, scenario):
    context.SUT = SUT()

    # TODO : need a way to define these easier, and then have environment
    # bring them in
    context.SUT.sets.define_set_from_enumeration('soda', 'orange,coke,7up')
    context.SUT.sets.define_set_from_enumeration('prices', '75,55,19')
    context.SUT.sets.define_set_from_enumeration(
        'baby_name',
        'puppy,kid,kitten,foal')
    context.SUT.sets.define_set_from_enumeration(
        'animal_name',
        'dog,goat,cat,horse')
    context.SUT.sets.define_set_from_enumeration(
        'domain_name',
        'localhost,gateway,google-dns')
    context.SUT.sets.define_set_from_enumeration(
        'ip',
        '127.0.0.1,192.168.1.1,8.8.8.8')
    context.SUT.sets.define_set_from_enumeration(
        'names',
        'Alice,Bob,Carol,Dave,empty')
    context.SUT.sets.define_set_from_enumeration('rooms', '1,2,3,penthouse')

    # TODO : need a way to define these easier, and then have environment bring them in
    # TODO : these don't have a property yet
    context.SUT.functions.define_function('pricing', 'soda', 'prices')
    context.SUT.functions.define_function('guests', 'rooms', 'names')

    # TODO : need a way to initialize functions
    context.SUT.functions.map('guests', '1', 'empty')
    context.SUT.functions.map('guests', '2', 'empty')
    context.SUT.functions.map('guests', '3', 'empty')
    context.SUT.functions.map('guests', 'penthouse', 'empty')

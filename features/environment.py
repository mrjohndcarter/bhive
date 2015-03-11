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

register_type(Number=parse_number)
register_type(Set=parse_set)
register_type(Enumeration=parse_enumeration)
register_type(Element=parse_element)
register_type(Function=parse_function)

# setup / teardown stuff

def before_scenario(context, scenario):
    context.SUT = SUT()
    context.SUT.sets.define_set_from_enumeration('soda', 'orange,coke,7up')
    context.SUT.sets.define_set_from_enumeration('prices', '75,55,19')

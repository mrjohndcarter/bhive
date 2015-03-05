from SUT import SUT

from behave import register_type

def register_set(context, name, definition):
    context.sets[name] = definition

def parse_number(text):
    return int(text)

register_type(Number=parse_number)

def parse_set(text):
    return text

def parse_enumeration(text):
    return text

def parse_element(text):
    return text

register_type(Set=parse_set)
register_type(Enumeration=parse_enumeration)
register_type(Element=parse_element)

def before_all(context):
    context.SUT = SUT()
    pass

def after_all(context):
    pass

def before_scenario(context, scenario):
    context.SUT = SUT()

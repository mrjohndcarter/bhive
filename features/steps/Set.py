from behave import given, when, then

@given(u'the set {set_:Set} is not defined')
def step_impl(context, set_):
    assert context.SUT.is_set_defined(set_) == False

@when(u'we define {set_:Set} with {elements:Enumeration}')
def step_impl(context, set_, elements):
    context.SUT.define_set_from_enumeration(set_, elements)

@then(u'the cardinality for {set_:Set} should be {card:Number}')
def step_impl(context, set_, card):
    assert context.SUT.get_set_cardinality(set_) == card

@then(u'the set {set_:Set} should contain element {element:Element}')
def step_impl(context, set_, element):
    assert context.SUT.set_contains(set_, element)

@then(u'the set {set_:Set} should not contain element {element:Element}')
def step_impl(context, set_, element):
    assert context.SUT.set_contains(set_, element) == False

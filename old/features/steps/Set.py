from behave import given, when, then


@given(u'the set {set_:Set} is not defined')
def step_impl(context, set_):
    assert context.SUT.sets.is_set_defined(set_) == False


@given(u'the set {set_:Set} contains element {element:Element}')
def step_impl(context, set_, element):
    assert context.SUT.sets.set_contains(set_, element) == True


@when(u'we define {set_:Set} with {elements:Enumeration}')
def step_impl(context, set_, elements):
    context.SUT.sets.define_set_from_enumeration(set_, elements)


@then(u'the cardinality for {set_:Set} is {card:Number}')
def step_impl(context, set_, card):
    assert context.SUT.sets.get_set_cardinality(set_) == card


@then(u'the set {set_:Set} contains element {element:Element}')
def step_impl(context, set_, element):
    assert context.SUT.sets.set_contains(set_, element) == True


@then(u'the set {set_:Set} should not contain element {element:Element}')
def step_impl(context, set_, element):
    assert context.SUT.sets.set_contains(set_, element) == False
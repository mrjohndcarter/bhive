from behave import *

@given(u'the set {set:Set} is not defined')
def step_impl(context, set):
    assert context.SUT.defined(set) == False

@when(u'we define {set:Set} with {elements:Enumeration}')
def step_impl(context, set, elements):
    context.SUT.define_set(set, elements)

@then(u'the cardinality for {set:Set} should be {card:Number}')
def step_impl(context, set, card):
    assert context.SUT.get_cardinality(set) == card

@then(u'the set {set:Set} should contain element {element:Element}')
def step_impl(context, set, element):
    assert context.SUT.contains(set, element)

@then(u'the set {set:Set} should not contain element {element:Element}')
def step_impl(context, set, element):
    assert context.SUT.contains(set, element) == False

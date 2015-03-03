from behave import *

@given(u'the set colors is not defined')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given the set colors is not defined')

@when(u'we define colors with \'red,blue,green\'')
def step_impl(context):
    raise NotImplementedError(u'STEP: When we define colors with \'red,blue,green\'')

@then(u'the cardinality should be 3')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the cardinality should be 3')

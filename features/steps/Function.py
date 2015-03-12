from behave import given, when, then

@given(u'Function {function:Function} is not defined')
def step_impl(context, function):
    assert context.SUT.functions.is_function_defined(function) == False

@given(u'Set {set_:Set} is defined')
def step_impl(context, set_):
    assert context.SUT.sets.is_set_defined(set_) == True

@given(u'Function {function:Function} is defined')
def step_impl(context, function):
    assert context.SUT.functions.is_function_defined(function) == True

@when(u'We define {function:Function} from {set_domain:Set} to {set_range:Set}')
def step_impl(context, function, set_domain, set_range):
    context.SUT.functions.define_function(function, set_domain, set_range)

@then(u'Function {function:Function} should be defined')
def step_impl(context, function):
    assert context.SUT.functions.is_function_defined(function) == True

@then(u'Range of {function:Function} should be {range_:Set}')
def step_impl(context, function, range_):
    assert context.SUT.functions.range(function) == range_

@then(u'Domain of {function:Function} should be {domain:Set}')
def step_impl(context, function, domain):
    assert context.SUT.functions.domain(function) == domain

@when(u'we map {d:Element} to {r:Element} in {function:Function}')
def step_impl(context, d, r, function):
    context.SUT.functions.map(function, d, r)

@then(u'{function:Function} should return {r:Element} for {d:Element}')
def step_impl(context, function, r, d):
    assert context.SUT.functions.function_return(function,d) == r

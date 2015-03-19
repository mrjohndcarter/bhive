from behave import given, when, then

# TODO : checks into is really just a 'curried' map(guests, nn, rr)
# can we auto define this?

@when(u'{nn:Element} checks into {rr:Set}')
def step_impl(context, nn, rr):
    context.SUT.functions.map('guests', rr, nn)

@given(u'{nn:Element} checked into {rr:Element}')
def step_impl(context, nn, rr):
    context.SUT.functions.map('guests', rr, nn)

@when(u'{nn:Element} checks out of {rr:Element}')
def step_impl(context, nn, rr):
    context.SUT.functions.map('guests', rr, 'empty')

@when(u'Range of {function_:Function} contains element {rr:Element}')
def step_impl(context, function_, rr):
    function_range = context.SUT.functions.range(function_)
    assert context.SUT.sets.set_contains(function_range, rr) == True

@then(u'{rr:Element} returns empty')
def step_impl(context, rr):
    assert context.SUT.functions.function_return('guests', rr) == 'empty'

@then(u'{rr:Element} is present.')
def step_impl(context, rr):
    function_range = context.SUT.functions.range('guests')
    assert context.SUT.sets.set_contains(function_range, rr) == True

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

@then(u'{rr:Element} returns empty')
def step_impl(context, rr):
    assert context.SUT.functions.function_return('guests', rr) == 'empty'

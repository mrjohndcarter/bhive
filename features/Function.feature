Feature: Defining Functions

As a specifier
I want to be able to specify a function using previously defined sets
So we can use the function in specifications

@wip
Scenario Outline: Defining a function

    Given Function <f> is not defined
    And Set <domain> is defined
    And Set <range> is defined
    When We define <f> from <domain> to <range>
    Then Function <f> should be defined
    And Range of <f> should be <range>
    And Domain of <f> should be <domain>

Examples:

    | f          | domain        | range             |
    | pricing    | soda          | prices            |

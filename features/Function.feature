Feature: Defining Functions

As a specifier
I want to be able to specify a function using previously defined sets
So we can use the function in specifications

Scenario Outline: Defining a function

    Given Function <f> is not defined
    And Set <domain> is defined
    And Set <range> is defined
    When We define <f> from <domain> to <range>
    Then Function <f> should be defined
    And Range of <f> should be <range>
    And Domain of <f> should be <domain>

Examples:

    | f          | domain           | range         |
    | parents    | baby_name        | animal_name   |
    | dns        | domain_name      | ip            |

Scenario Outline: Adding to a function

    Given Function <f> is defined
    And the set <domain> should contain element <d>
    And the set <range> should contain element <r>
    When we map <d> to <r> in <f>
    Then <f> should return <r> for <d>

Examples:

    | f          | domain   | range  |  d       |   r   |
    | pricing    | soda     | prices |  orange  |   55  |

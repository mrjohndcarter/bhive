Feature: Defining a set

    As a developer
    I want to be able to specify a set using a string
    So we can use the set in relations.

Scenario Outline:   Defining a Set

    Given the set <s> is not defined
    When we define <s> with <comprehension>
    Then the cardinality should be <c>

Examples:

        |  s        |  comprehension        | c     |
        |  colors   |  'red,blue,green'     | 3     |

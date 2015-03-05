Feature: Defining a set

    As a developer
    I want to be able to specify a set using a string
    So we can use the set in relations.

Scenario Outline:   Defining a Set With Enumeration

    Given the set <s> is not defined
    When we define <s> with <enumeration>
    Then the cardinality for <s> should be <c>

Examples:

        |  s            |  enumeration              | c     |
        |  Colors       |  red,blue,green           | 3     |

Scenario Outline:   Testing Set Membership

    Given the set <s> is not defined
    When we define <s> with <enumeration>
    Then the set <s> should contain element <e>

Examples:

        |  s            |  enumeration              | e       |
        |  Colors       |  red,blue,green           | red     |

Scenario Outline:   Testing Set Non-Membership

    Given the set <s> is not defined
    When we define <s> with <enumeration>
    Then the set <s> should not contain element <e>

Examples:

        |  s            |  enumeration              | e         |
        |  Colors       |  red,blue,green           | purple    |

Feature: Hotel Guest Registration

    As a front desk person
    I want to be able to track who is staying and their room
    So that I can find people and manage room allocations

Scenario Outline: Guest Checkin

    Given Set names is defined
    and Set rooms is defined
    and Function guests is defined
    and the Set names should contain element <name>
    and the Set rooms should contain element <room>
    when <name> checks into <room>
    then guests returns <name> for <room>

Examples:

|   name    |   room    |
|   Alice   |   2       |
|   Bob     |   3       |

Scenario Outline: Guest Checkout

    Given Set names is defined
    and Set rooms is defined
    and Function guests is defined
    and <name> checked into <room>
    when <name> checks out of <room>
    then <room> returns empty

Examples:

|   name    |   room    |
|   Alice   |   2       |
|   Bob     |   3       |

Scenario: Guest Query

Scenario: Present Query

Scneario: Swap Guests

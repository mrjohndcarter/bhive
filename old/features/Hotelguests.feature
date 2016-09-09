Feature: Hotel Guest Registration

  As a front desk person
  I want to be able to track who is staying and their room
  So that I can find people and manage room allocations

  Scenario Outline: Guest Checkin

    Given Set names is defined
  and Set rooms is defined
  and Function guests is defined
  and the Set names contains element <name>
  and the Set rooms contains element <room>
  when <name> checks into <room>
  then guests returns <name> for <room>

    Examples:

      | name  | room |
      | Alice | 2    |
      | Bob   | 3    |

  Scenario Outline: Guest Checkout

    Given Set names is defined
  and Set rooms is defined
  and Function guests is defined
  and <name> checked into <room>
  when <name> checks out of <room>
  then <room> returns empty

    Examples:

      | name  | room |
      | Alice | 2    |
      | Bob   | 3    |

  Scenario Outline: Guest Query

    Given <name> checked into <room>
  then a query for <room> returns <name>

    Examples:

      | name  | room |
      | Alice | 2    |
      | Bob   | 3    |

  Scenario Outline: Present Query

      # basically a type definition (INVARIANT)
    Given the Set names contains element <name>
  when Range of guests contains element <name>
  then <name> is present.
      # predicate, should have a way to enforce NOT

    Examples:

      | name  |
      | Alice |
      | Bob   |


  Scenario Outline: Swap Guests

    Given <name_a> checked into <room_a>
  and <name_b> checked into <room_b>
  when <room_a> is swapped with <room_b>
  then guests returns <name_b> for <room_a>
  and guests returns <name_a> for <room_b>

    Examples:

      | name_a | room_a    | name_b | room_b |
      | Alice  | 1         | Bob    | 3      |
      | Carol  | penthouse | Bob    | 3      |

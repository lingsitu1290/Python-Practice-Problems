"""Leaping lemur.

Calculate the fewest number of jumps the lemur needs to
jump to the last tree. The lemur can jump 1 or 2 branches.
It cannot use deadly branch (1 in the list).

    >>> lemur([0])
    0

    >>> lemur([0, 0])
    1

    >>> lemur([0, 0, 0])
    1

    >>> lemur([0, 1, 0])
    1

    >>> lemur([0, 0, 1, 0])
    2

    >>> lemur([0, 0, 0, 0, 1, 0, 0, 1, 0])
    5

while position < len(branches)-1:

Keep track of starting position. [0]
Keep a list of the positions. 
Return the length of the list as the number of jumps.

base case: when the list is 0 or 1 item: jump is 0
position has to be less than length of list
"""


def  lemur(branches):
    """Return number of jumps needed."""

    assert branches[0] == 0, "First branch must be alive"
    assert branches[-1] == 0, "Last branch must be alive"


    pos = 0

    jump_count = 0

    if len(branches) == 1:
        return 0 
    elif len(branches) == 2 or len(branches) == 3:
        return 1

    while pos != len(branches)-1:

        possible_branch = branches[pos+1:pos+3]
        if possible_branch[-1] == 0:
            pos += 2
            jump_count += 1
        elif possible_branch[0] == 0:
            pos += 1 
            jump_count += 1

    return jump_count

                 

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. NICE JUMPING!\n"
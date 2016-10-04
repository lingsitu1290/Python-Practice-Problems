# Reddit Whiteboarding 

import random 

def get_rnd(lst, n):
    """Return n random numbers from a list.

    Hard to test random but if given n equal to the length of lst. 
    Result will be full lst.

    >>> get_rnd([1,2,3], 3)
    [1, 2, 3]
    >>> get_rnd([1,2], 2)
    [1, 2]

    """

    result = []

    for i in range(n):
        num = random.choice(lst)
        result.append(num)
        lst.remove(num)

    return sorted(result)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
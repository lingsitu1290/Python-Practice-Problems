# Pixlee whiteboarding

def pasc(r, c):
    """ 
    Given the row and column. Find the number in the pascal triangle.

    >>> pasc(0,0)
    1

    >>> pasc(3,2)
    3

    >>> pasc(5,4)
    5

    """

    if c == 0 or c == r:
        return 1

    # Not needed
    if c == 1 or c == r-1:
        return r

    return pasc(r-1, c) + pasc(r-1, c-1)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
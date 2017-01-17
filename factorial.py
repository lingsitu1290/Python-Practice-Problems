def fact(n):
    """
    >>> fact(5)
    120
    >>> fact(3)
    6
    >>> fact(0)
    1
    """
    # Base case
    if n == 0:
        return 1

    else:
        return n * fact(n-1)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

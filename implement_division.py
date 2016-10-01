# implement division
# Given the numerator and demoninator, implement the division function
# Return quotient followed by remainder

def divide(num, demo):
    """
    >>> divide(100,10)
    10 0
    >>> divide(101,10)
    10 1
    """

    count = 0
    while num >= demo:
        num = num - demo
        count += 1

    print count, num

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
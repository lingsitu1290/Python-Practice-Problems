#Whiteboarding problems from 9/8/2016 and 9/9/2016 with Leslie


def odd(lst):
    """
    Return all odd numbers in a list
    >>> odd([1,2,3,4,5,6])
    1
    3
    5
    """

    for num in lst:
        if num % 2 != 0 :
            print num




if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
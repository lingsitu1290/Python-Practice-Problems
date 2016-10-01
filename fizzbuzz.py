def fizzbuzz():
    """Count from 1 to 20 in fizzbuzz fashion.

    >>> fizzbuzz()
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    """

    for num in range(1,21):
        if num % 3 == 0 and num % 5 == 0:
            print 'fizzbuzz'
        elif num % 3 == 0:
            print 'fizz'
        elif num % 5 == 0: 
            print 'buzz'
        else:
            print num


# Given number n
def fizzbuzz(n):
    """Count from 1 to 20 in fizzbuzz fashion.

    >>> fizzbuzz(20)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    17
    fizz
    19
    buzz
    """

    for i in range(1, n+1):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        print output or i


if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
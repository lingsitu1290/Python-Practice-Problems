def print_digits_backwards(number):
    """Given an integer, print each digit in reverse order.
    >>> print_digits_backwards(12345)
    5
    4
    3
    2
    1
    >>> print_digits_backwards(-2)
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
      File "hb-printdigitsbkwds.py", line 5, in print_digits_backwards
        assert number > 0, "Number should be a positive interger!"
    AssertionError: Number should be a positive interger!
    >>> print_digits_backwards(3)
    3

    >>>
    """
    # Assert number is a positive. If not 
    assert number > 0, "Number should be a positive interger!"

    num_string = str(number)

    for num in num_string[::-1]:
        print num


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
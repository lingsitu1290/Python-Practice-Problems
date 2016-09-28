def find_missing_num(lst, max_num):
    """Given a list of numbers from 1 to a maximum number, return the missing
    number in the list. 
    >>> find_missing_num([1, 2, 3, 4, 5, 6, 7, 9, 10], 10)
    8
    >>> find_missing_num([1, 2, 6, 7, 8, 10, 3, 4, 9], 10)
    5

    Time: O(n)
    """

    for num in range(1,max_num+1):
        if num not in lst:
            return num

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
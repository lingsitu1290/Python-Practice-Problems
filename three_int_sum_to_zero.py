# Pixlee Whiteboarding 

def three_int_sum_to_zero1(lst):
    """
    Determine if any 3 integers in an array sum to 0. 

    >>> three_int_sum_to_zero1([1,-1,3,5,2,-2])
    True
    >>> three_int_sum_to_zero1([2,3,4,5,-1,2])
    False
    """

    for i in lst:
        for j in lst:
            for k in lst:
                if lst[i] + lst[j] + lst[k] == 0:
                    return True
        return False

def three_int_sum_to_zero2(lst):
    """
    Determine if any 3 integers in an array sum to 0. 

    >>> three_int_sum_to_zero2([1,-1,3,5,2,-2])
    True
    >>> three_int_sum_to_zero2([2,3,4,5,-1,2])
    False
    """

    for i in lst:
        for j in lst[i:]:
            for k in lst[j:]:
                total = lst[i] + lst[j] + lst[k]
                if total is not 0:
                    pass
                else:
                    return True
        return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
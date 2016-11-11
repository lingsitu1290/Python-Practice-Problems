# Pixlee Whiteboarding 

def three_int_sum_to_zero1(lst):
    """
    Determine if any 3 integers in an array sum to 0. 

    #>>> three_int_sum_to_zero1([0,1,2,-1,3,5,2,-2])
    #True
    #>>> three_int_sum_to_zero1([2,3,4,5,-1,2])
    #False
    >>> three_int_sum_to_zero1([2,0,1,9,0])
    False

    """

    for i, num in enumerate(lst):
        for j, num1 in enumerate(lst):
            for k, num2 in enumerate(lst):
                #print i, num, j, num1, k, num2
                if i == j or j == k or i == k:
                    continue
                if lst[i] + lst[j] + lst[k] == 0:
                    return True
    return False

def three_int_sum_to_zero2(lst):
    """
    Determine if any 3 integers in an array sum to 0. 

    #>>> three_int_sum_to_zero2([0,1,-1,3,5,2,-2])
    #True
    # >>> three_int_sum_to_zero2([2,3,4,5,-1,2])
    # False
    >>> three_int_sum_to_zero2([2,3,1,9,0,0])
    False

    """

    for i, num in enumerate(lst):
        sublst = lst[i+1:]
        for j, num1 in enumerate(sublst):
            subsublst = sublst[j+1:]
            for k, num2 in enumerate(subsublst):
                total = num + num1 + num2
                #  print i, num, j, num1, k, num2
                if total is  0:
                    return True
    return False

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. WOWZA!\n"
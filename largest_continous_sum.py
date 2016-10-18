def largest_cont_sum(lst):
    """ Given an array of positive and negative numbers. 
    Find the largest continous sum.

    >>> largest_cont_sum([1,2,3,4,-1])
    10
    >>> largest_cont_sum([])
    0
    >>> largest_cont_sum([10,2,5,6,-10,-1,12])
    24
    >>> largest_cont_sum([-1,-2,-5,-1])
    -1
    """

    # Edge case: if nothing in list
    if len(lst) == 0:
        return 0

    # start max_sum and current_sum at the first index
    max_sum = current_sum = lst[0]

    for num in lst[1:]:
        current_sum = max(current_sum+num,num)

        max_sum = max(current_sum, max_sum)

    return max_sum


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. EXCELLENT!\n"
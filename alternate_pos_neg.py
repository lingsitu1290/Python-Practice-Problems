def alternate_pos_neg(num_list):
    """
    Given a list of numbers, returns a list with alternating positive and negative
    numbers while maintaining order. If there are more positive numbers than negative 
    numbers, they appear at the end of the array, and vice versa.
    >>> alternate_pos_neg([1, 2, 3, -4, -1, 4])
    [1, -4, 2, -1, 3, 4]
    >>> alternate_pos_neg([-5, -2, 5, 2, 4, 7, 1, 8, 0, -8])
    [5, -5, 2, -2, 4, -8, 7, 1, 8, 0]
    >>> alternate_pos_neg([-1, -2, 3, -4])
    [3, -1, -2, -4]
    """

    pos_nums = []
    neg_nums = [] 
    result = []

    for num in num_list: 
        if num < 0: 
            neg_nums.append(num)
        else: 
            pos_nums.append(num)

    i = 0
    j = 0

    while i < len(pos_nums) or j < len(neg_nums):
        if i < len(pos_nums):
            result.append(pos_nums[i])
        if j < len(neg_nums):
            result.append(neg_nums[j])
        i += 1
        j += 1

    return result


if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
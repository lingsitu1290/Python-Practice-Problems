def sum_list(num_lst):
    """Sum numbers in a list recursively.

    >>> sum_list([1,2,3]) 
    6
    >>> sum_list([4,5,6])
    15
    """

    # Only one item in the list. Return the item
    if len(num_lst) == 1:
        return num_lst[0]
        
    return num_lst[0] + sum_list(num_lst[1:])


if __name__ == "__main__":
    import doctest
    if not doctest.testmod().failed:
        print "\n*** ALL TESTS PASS; YOU MUST BE JUMPING WITH JOY\n"
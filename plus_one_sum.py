"""
Write a function that takes an array of integers and returns the sum of
the integers after adding 1 to each.
"""
def plus_one_sum(lst):
    """
    >>> plus_one_sum([1, 2, 3, 4])
    14
    >>> plus_one_sum([4, 5, 6, 7])
    26
    """

    # Add 1 to each number in the list in place then sum new list
    for i, num in enumerate(lst):
        lst[i] = num + 1

    return sum(lst)

def plus_one_sum_2(lst):
    """
    >>> plus_one_sum_2([1, 2, 3, 4])
    14
    >>> plus_one_sum([4, 5, 6, 7])
    26
    """

    return sum(lst) + len(lst)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

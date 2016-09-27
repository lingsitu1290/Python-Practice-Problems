def sort_sorted_lists(a, b):
    """
    Given already sorted lists, list a and list b, respectively, return a new
    list that is a merge sort of list a and b. NO .sort() or .sorted()
    >>> sort_sorted_lists([1, 2, 4, 7], [3, 5, 6, 8])
    [1, 2, 3, 4, 5, 6, 7, 8]
    >>> sort_sorted_lists([3, 5, 8], [1, 2, 6, 10])
    [1, 2, 3, 5, 6, 8, 10]

    Time: O(n)
    Space: O(n)
    """

    # Using merge sort

    merged_list = []

    # While there are still numbers in either a or b
    while len(a) > 0 or len(b) > 0: 
        # If a is an empty list, pop the first number of b
        if a == []:
            merged_list.append(b.pop(0))
        # If b is an empty list, pop the first number of a 
        elif b == []:
            merged_list.append(a.pop(0))
        # If the first number in b is greater than the first in a, pop the first of a 
        elif a[0] < b[0]:
            merged_list.append(a.pop(0))
        # If the first number in a is greater than the first in b, pop the first of b
        else: 
            merged_list.append(b.pop(0))

    return merged_list

def sort_sorted_lists(a, b):
    """
    Given already sorted lists, list a and list b, respectively, return a new
    list that is a merge sort of list a and b. NO .sort() or .sorted()
    >>> sort_sorted_lists([1, 2, 5], [3, 4, 6, 7, 10])
    [1, 2, 3, 4, 5, 6, 7, 10]
    >>> sort_sorted_lists([3, 6, 8], [1, 2, 7, 10])
    [1, 2, 3, 6, 7, 8, 10]
    """

    merged_list = []

    # Start indexes for both list at 0
    a_index = 0
    b_index = 0 

    # While the indexes are less than the length of a or b
    while a_index < len(a) and b_index < len(b):
        # If number at a is greater than b, add value at b to list and increment b index
        if a[a_index] > b[b_index]:
            merged_list.append(b[b_index])
            b_index += 1 
        # If number at b is greater than a, add value at a to list and increment a index
        else: 
            merged_list.append(a[a_index])
            a_index += 1

    # Add the rest of a or b if there are still numbers
    merged_list.extend(a[a_index:])
    merged_list.extend(b[b_index:])

    return merged_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
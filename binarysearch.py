"""
Using binary search to see if a value exists in an ordered list.
"""

def binary_search(list, val, found=False):
    """
    >>> binary_search([1,2,3,4,5,6,7,8], 2)
    True
    >>> binary_search([1,2,3,4,5,6,7,8], 11)
    False
    >>> binary_search([1,2,3,4,5,6,7,8], 8)
    True
    """

    first = 0
    last = len(list) - 1

    while first <= last and not found:
        mid = (first+last)/2

        if list[mid] == val:
            found = True
        else:
            if val < list[mid]:
                last = mid -1
            else:
                first = mid + 1

    return found

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YOU'RE TERRIFIC AT THIS!\n"

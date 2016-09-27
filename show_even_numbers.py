def show_even_numbers(lst):
    """Given a list of even and odd numbers, return a list of the indices at
        which the original number is an even number.

    >>> show_even_numbers([1,2,3,4,5,6,7,8,9])
    [1, 3, 5, 7]

    Time: O(n)
    Space: O(n)
    """
    even_index_list = []

    for i, val in enumerate(lst):
        if val % 2 == 0:
            even_index_list.append(i)

    print even_index_list

def show_even_numbers(lst):
    """Given a list of even and odd numbers, return a list of the indices at
        which the original number is an even number.

    >>> show_even_numbers([2,4,6,8,10])
    [0, 1, 2, 3, 4]

    Time: O(n)
    Space: O(n)
    """
    even_index_list = []

    i = 0 

    for num in lst: 
        if num % 2 == 0:
            even_index_list.append(i)
            i += 1

    print even_index_list

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
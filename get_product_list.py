# Interview Cake 

def get_product_list(lst):
    """
    Given a list of integers, write a function that takes a list of integers
    and returns a list of the products (product of every integer except the
    integer at that index).
    For example, given:
      [1, 7, 3, 4]
    your function would return:
      [84, 12, 28, 21]
    by calculating:
      [7*3*4, 1*3*4, 1*7*4, 1*7*3]
    Do not use division in your solution.

    >>> get_product_list([1, 7, 3, 4])
    [84, 12, 28, 21]

    >>> get_product_list([])
    []
    """

    product_list = []

    # loop through length of the list 
    for i in range(len(lst)):
        j = 0 
        product = 1
        while j < len(lst):
            # If we are not at the same index, multiply to product and increment
            if j != i: 
                product *= lst[j]
                j += 1
            else:           
                j += 1
        product_list.append(product)
    return product_list

def get_products_of_all_ints_except_at_index_v2(lst):
    """
    >>> get_products_of_all_ints_except_at_index_v2([1, 7, 3, 4])
    [84, 12, 28, 21]
    """

    result = []

    for i, num in enumerate(lst):
        total = 1
        for j, num in enumerate(lst):
            if j != i:
                total *= lst[j]

        result.append(total)

    return result


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"

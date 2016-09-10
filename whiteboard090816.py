#Whiteboarding problems from 9/8/2016 and 9/9/2016 with Leslie

def odd(lst):
    """
    Return all odd numbers in a list
    >>> odd([1,2,3,4,5,6])
    1
    3
    5

    O(n)
    """

    for num in lst:
        if num % 2 != 0:
            print num

def print_index_item(lst):
    """
    Given list, return the index and number.
    >>> print_index_item([3, 4, 8])
    0 3
    1 4
    2 8

    O(n)
    """

    i = 0
    for item in lst:
        print i, lst[i]
        i = i + 1

def words_with_length(lst,num):
    """
    Given a list of words and a number. 
    Return a list of words with the length of the number given.
    >>> words_with_length(['apple', 'cherry', 'berry', 'mochi'], 5)
    ['apple', 'berry', 'mochi']

    O(n)
    """

    final_list = []

    for word in lst:
        if len(word) == num:
            final_list.append(word)
    return final_list

def common_between_two_lists(lst1, lst2):
    """
    Given two lists. Return list of common items between the two lists.
    >>> common_between_two_lists([1,2,3,4,8], [1,5,6,8])
    [1, 8]

    O(n^2)
    """

    common = [] 

    for i in lst1:
        for j in lst2:
            if i == j:
                common.append(i)

    return common

def remove_duplicates(lst):
    """
    Given a list of words, return a list with the duplicates removed.
    >>> remove_duplicates(['apple','berry','berry','cherry','durian'])
    ['apple', 'berry', 'cherry', 'durian']
    >>> remove_duplicates([])
    []

    O(n)
    """
    
    no_duplicates = []

    if len(lst) == 0:
        return []

    for item in lst:
        if item not in no_duplicates:
            no_duplicates.append(item)

    return no_duplicates

def reverse(lst):
    """
    Given a list. Reverse items in place.
    >>> reverse([1, 'apple', 'durian', 3])
    [3, 'durian', 'apple', 1]

    O(n)
    """

    i = 0 

    for i in range(int(len(lst)/2)):
        lst[i], lst[-(i + 1)] = lst[-(i + 1)], lst[i]

    return lst


def is_prime(num):
    """
    Given an integer. Returns true or false if number is prime.
    >>> is_prime(5)
    True
    >>> is_prime(4)
    False

    O(n)
    """

    for i in range(2,num):
        if num % i == 0:
            return False
        else:
            return True


if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
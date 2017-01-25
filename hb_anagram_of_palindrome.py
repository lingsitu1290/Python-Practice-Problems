def is_anagram_of_palindrome(string):
    """
    Return whether the given string is an anagram of a palindrome.
    >>> is_anagram_of_palindrome("a")
    True

    >>> is_anagram_of_palindrome("ab")
    False

    >>> is_anagram_of_palindrome("aab")
    True

    >>> is_anagram_of_palindrome("arceace")
    True

    >>> is_anagram_of_palindrome("arceaceb")
    False
    """

    count = {}

    for word in string:
        count[word] = count.get(word, 0)+1

    # Without using .get
    # for word in string:
    #     if word in count:
    #         count[word] += 1
    #     else:
    #         count[word] = 1

    odd_counts = 0

    for count in count.values():
        if count % 2 == 1:
            odd_counts += 1
    return odd_counts <= 1

def is_anagram_of_palindrome_v2(string):
    """
    Return whether the given string is an anagram of a palindrome.
    >>> is_anagram_of_palindrome_v2("a")
    True

    >>> is_anagram_of_palindrome_v2("ab")
    False

    >>> is_anagram_of_palindrome_v2("aab")
    True

    >>> is_anagram_of_palindrome_v2("arceace")
    True

    >>> is_anagram_of_palindrome_v2("arceaceb")
    False
    """

    count = {}

    for word in string:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    # Check if palindrome

    if_odd = False

    for count in count.values():
        if count % 2 != 0:
            if if_odd:
                return False
            if_odd = True
    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"

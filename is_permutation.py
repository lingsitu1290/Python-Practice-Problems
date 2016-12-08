
def is_permutation(string1, string2):
    """
    >>> is_permutation("abcd", "dbca")
    True
    >>> is_permutation("abcd", "efgh")
    False
    >>> is_permutation("cat", "sat")
    False
    >>> is_permutation("happy", "yppah")
    True
    """
    sorted_string1 = sorted(string1)
    sorted_string2 = sorted(string2)

    if sorted_string1 == sorted_string2:
        return True
    return False


def is_permutation2(string1, string2):
    """
    >>> is_permutation2("abcd", "dbca")
    True
    >>> is_permutation2("abcd", "efgh")
    False
    >>> is_permutation2("cat", "sat")
    False
    >>> is_permutation2("happy", "yppah")
    True
    """
    string_dict = {}

    for letter in string1:
        if letter not in string_dict:
            string_dict[letter] = string_dict.get(letter, 1)
        else:
            string_dict[letter] += 1

    for letter in string2:
        if letter in string_dict:
            string_dict[letter] -= 1
        else:
            string_dict[letter] = string_dict.get(letter, 1)

    # print string_dict
    for k, v in string_dict.iteritems():
        if v != 0:
            return False
    return True


def is_permutation3(string1, string2):
    """
    >>> is_permutation3("abcd", "dbca")
    True
    >>> is_permutation3("abcd", "efgh")
    False
    >>> is_permutation3("cat", "sat")
    False
    >>> is_permutation3("happy", "yppah")
    True
    """
    string1_dict = {}
    string2_dict = {}

    for letter in string1:
        if letter not in string1_dict:
            string1_dict[letter] = string1_dict.get(letter, 1)
        else:
            string1_dict[letter] += 1

    for letter in string2:
        if letter in string2_dict:
            string2_dict[letter] += 1
        else:
            string2_dict[letter] = string2_dict.get(letter, 1)

    if string1_dict == string2_dict:
        return True
    return False


if __name__ == "__main__":
    import doctest
    doctest.testmod()
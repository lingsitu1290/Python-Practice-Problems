def reverse_vowels(string):
    """
    Given a string, reverse the vowels (does not include "y").
    >>> reverse_vowels("hello")
    'holle'
    >>> reverse_vowels("tower")
    'tewor'

    Time: O(n)
    Space: O(n)
    """

    vowels = ['a','e','i','o','u']

    vowel_index = []

    for val in string:
        if val in vowels: 
            vowel_index.append(string.index(val))

    string_list = list(string)

    i = vowel_index[0]
    j = vowel_index[1]

    return "".join((string[:i], string[j], string[i+1:j], string[i], string[j+1:]))

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
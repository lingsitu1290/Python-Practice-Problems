def compress(string):
    """
    >>> compress("aabcccccaaa")
    'a2b1c5a3'
    >>> compress("aabbba")
    'a2b3a1'
    >>> compress("abcdefg")
    'abcdefg'
    >>> compress("abcdddeff")
    'a1b1c1d3e1f2'
    >>> compress("abcff")
    'a1b1c1f2'
    """

    past_chars = [string[0]]
    char_counts = [1]

    for i in range(1, len(string)):
        if string[i] == past_chars[-1]:
            char_counts[-1] += 1
        else:
            past_chars.append(string[i])
            char_counts.append(1)

    compressed_string = ""

    # list_of_ones = []
    # for i in range(len(string)):
    #     list_of_ones.append(1)
    list_of_ones = [1 for x in range(len(string))]

    if char_counts == list_of_ones:
        return string
    else:
        for char, count in zip(past_chars, char_counts):
            compressed_string += char + str(count)


    return compressed_string

def compress_v2(string):
    """
    >>> compress_v2("aabcccccaaa")
    'a2b1c5a3'
    >>> compress_v2("aabbba")
    'a2b3a1'
    >>> compress_v2("abcdefg")
    'a1b1c1d1e1f1g1'
    >>> compress_v2("abcdddeff")
    'a1b1c1d3e1f2'
    >>> compress_v2("abcff")
    'a1b1c1f2'
    >>> compress_v2("a")
    'a1'
    >>> compress_v2("")
    ''
    """

    result = ""

    l = len(string)

    # Edge cases
    if l == 0:
        return ""

    if l == 1:
        return string + "1"

    last = string[0]
    count = 1
    i = 1

    while i < l:
        if string[i] == string[i-1]:
            count += 1
        else:
            result = result + string[i-1] + str(count)
            count = 1

        i += 1

    # For the last letter
    result = result + string[i-1] + str(count)

    return result

## This version only works IF same letters are clustered together
import collections

def compress_v3(string):
    """
    >>> compress_v3("aabccccc")
    'a2b1c5'
    >>> compress_v3("aabbb")
    'a2b3'
    >>> compress_v3("abcdefg")
    'a1b1c1d1e1f1g1'
    >>> compress_v3("abcdddeff")
    'a1b1c1d3e1f2'
    >>> compress_v3("abcff")
    'a1b1c1f2'
    >>> compress_v3("a")
    'a1'
    >>> compress_v3("")
    ''
    """

    string_dict = collections.OrderedDict()
    final = ""

    for letter in string:
        string_dict[letter] = string_dict.get(letter, 0)+1

    for letter, count in string_dict.iteritems():
        final += letter + str(count)

    return final

#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

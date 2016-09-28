def group_anagrams(lst):
    """
    Given a list of strings, group the strings that are anagrams of each other together.
    >>> group_anagrams(["cat", "dog", "god", "banana", "odg"])
    [['banana'], ['dog', 'god', 'odg'], ['cat']]
    >>> group_anagrams(["tire", "iret", "sam", "ams", "car"])
    [['tire', 'iret'], ['car'], ['sam', 'ams']]

    Time: O(n)
    """
    anagrams_dict = {}

    for word in lst:
        # Sort the words to see check for anagrams
        sorted_word = "".join(sorted(word))

        # If sorted word in already in dictionary append to the list else create new list with word
        if sorted_word in anagrams_dict:
            anagrams_dict[sorted_word].append(word)
        else:
            anagrams_dict[sorted_word] = [word]

    # Return list of anagrams
    print anagrams_dict.values()

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"

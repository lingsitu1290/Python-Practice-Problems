def anagram(s1, s2):

    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

def anagram2(s1, s2):

    # Clean up strings
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    # Edge case
    if len(s1) != len(s2):
        return False

    count = {}

    # Store the count and letter in the count dictionary
    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    # Start deleting the count for s2 
    for letter in s2: 
        if letter in count: 
            count[letter] -= 1
        else:
            count[letter] = 1

    for k in count: 
        if count[k] != 0:
            return False

    return True

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED\n"

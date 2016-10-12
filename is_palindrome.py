def is_palindrome(string):
    """
    Function to see if word is a palindrome. 
    
    >>> is_palindrome("racecar")
    True
    >>> is_palindrome("chicken")
    False
    """

    if string == string[::-1]:
        return True
    return False

def is_palindrome2(string):
    """
    Function to see if word is a palindrome. 
    
    >>> is_palindrome2("racecar")
    True
    >>> is_palindrome2("chicken")
    False
    """

    for i in range(len(string)/2):
        if string[i] != string[-i-1]:
            return False
    return True


def is_palindrome_optimized(str1):
    """
    Check if word is a palindrome. Including possible spaces and punctuation. 

    >>> is_palindrome_optimized('nurses run')
    True
    >>> is_palindrome_optimized('ra,ce.car')
    True
    >>> is_palindrome_optimized('hello world')
    False
    """

    import string

    str1 = str1.replace(' ','')
    # only want characters in str1 using list comprehension
    str1 = ''.join(letter for letter in str1 if letter not in string.punctuation)
    if str1 == str1[::-1]:
        return True
    return False




if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
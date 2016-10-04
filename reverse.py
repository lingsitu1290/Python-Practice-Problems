# Reverse strings 

def reverse(string):
    """
    >>> reverse("back")
    kcab
    """

    print string[::-1]

#Time: O(n)
#Space: O(n)

def reverse(string):
    """
    >>> reverse("cheese")
    'eseehc'
    """

    string1 = ""

    for i in range(1,len(string)+1):
        string1 += string[i*-1]

    return string1

def reverse(string):
    """
    >>> reverse("hello")
    'olleh'
    """
    string1 = ""

    for char in string: 
        string1 = char + string1

    return string1

# Swtiching indexes
def reverse(string):
    """
    >>> reverse("sushi")
    'ihsus'
    """
    length = len(string)
    string_list = list(string)

    for i in range(len(string)/2):
        string_list[i], string_list[-i-1] = string_list[-i-1], string_list[i]

    return "".join(string_list)


#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()
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

# Swtiching indexes reverse in place without a temp variable
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

# Reverse in place Implemention #2 using a temp variable
def reverse_2(string):
    """
    >>> reverse_2('moose')
    'esoom'
    """

    string_list = list(string)
    length = len(string)

    for i in range(length/2):
        temp = string_list[i]
        string_list[i] = string_list[-i-1]
        string_list[-i-1] = temp

    return "".join(string_list)

# Third implementation of reverse in place difference in indexing
def reverse_2(string):
    """
    >>> reverse_2('moose')
    'esoom'
    """

    string_list = list(string)
    length = len(string)

    for i in range(length/2):
        temp = string_list[i]
        string_list[i] = string_list[length-1-i]
        string_list[length-1-i] = temp

    return "".join(string_list)



#################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()

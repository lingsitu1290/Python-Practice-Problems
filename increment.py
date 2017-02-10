"""
Function that receives an array of single digit ints representing a longer
integer, such as [8, 7, 9, 9] representing 8,799, and increments it by 1
returning the result also in an array format.
"""

def increment(lst):
    """
    >>> increment([8, 7, 9, 9])
    [8, 8, 0, 0]
    """

    string = ""

    for num in lst:
        string += str(num)

    number = int(string)

    final_num = number + 1

    final_lst = []

    for num in str(final_num):
        final_lst.append(int(num))

    return final_lst

if __name__ == "__main__":
    import doctest
    doctest.testmod()

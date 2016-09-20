# Time: O(n)
# Space: O(1)
def find_max(lst):
    """
    Function that takes in a list of numbers and return the highest numbers.

    >>> find_max([1,3,2])
    3
    >>> find_max([])
    
    >>> find_max([-3,-2,0])
    0
    """

    if len(lst) == 0: 
        return
    else: 
        max = lst[0]

    for num in lst: 
        if num > max:
            max = num 
    return max

if __name__ == "__main__":
    import doctest
    doctest.testmod()
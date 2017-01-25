"""
Given an unlimited number of pennies and dimes and the number of coins.
Write a function that returns the total amount for each combination of coins
given the number of coins.
"""

def get_coins(num):
    """
    >>> get_coins(3)
    [3, 12, 21, 30]
    >>> get_coins(2)
    [2, 11, 20]
    """
    amounts = set()

    dime = 10
    i = 0
    while i <= num:

        total = i + ((num - i) * dime)
        amounts.add(total)
        i+=1

    return list(amounts)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

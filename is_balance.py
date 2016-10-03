def is_balance(parens):

    """
    >>> is_balance('[]')
    True
    >>> is_balance('()(){]')
    False
    
    """

    if len(parens) % 2 != 0:
        return False

    opening = set('([{')
    matches = set([ ('(',')'), ('[',']'), ('{','}') ])

    stack = []

    for paren in parens: 

        if paren in opening:
            stack.append(paren)
        else:
            if len(stack) == 0:
                return False
            last_open = stack.pop()

            if (last_open, paren) not in matches:
                return False

    return len(stack) == 0

if __name__ == "__main__":
    import doctest
    doctest.testmod()
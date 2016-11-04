def balance_parens(parens):
    """
    Given a string of parentheses, return the string balanced

    >>> balance_parens('(())(')
    '(())()'
    >>> balance_parens('(()')
    '(())'
    >>> balance_parens('((()))')
    '((()))'
    """
    paren_stack = []
    balanced = ""

    for paren in parens:
        # if it an opening paren, we add to stack and to balanced string
        if paren == "(":
            paren_stack.append(paren)
            balanced += paren
        # paren == ")"
        else:
            # if there are opening parens, we pop from stack and add to balanced
            if paren_stack:
                paren_stack.pop()
            balanced += paren
    # while there are still things in the stack, we pop and balance with closing paren
    while paren_stack:
        paren_stack.pop()
        balanced += ")"

    return balanced


if __name__ == "__main__":
    import doctest
    doctest.testmod()

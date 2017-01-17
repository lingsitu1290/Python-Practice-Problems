def second_max_num(num_list):
    """
    Returns the second maximum number in the list; returns None otherwise
    >>> second_max_num([10, 4, -1, 7])
    7
    >>> second_max_num([-5, -2, 0])
    -2
    >>> second_max_num([1])
    """

    if len(num_list) < 2:
        return

    sorted_list = sorted(num_list)

    return sorted_list[-2]


def second_max_num2(num_list):
    """
    Returns the second maximum number in the list; returns None otherwise
    >>> second_max_num2([10, 4, -1, 7])
    7
    >>> second_max_num2([-5, -2, 0])
    -2
    >>> second_max_num2([1])
    """

    if len(num_list) < 2:
        return

    max_num = num_list[0]
    sec_num = num_list[1]

    for num in num_list:
        if num > max_num:
            sec_num = max_num
            max_num = num
        elif sec_num < num < max_num:
            sec_num = num

    return sec_num

# Weird way
def second_max_num3(num_list):
    """
    Returns the second maximum number in the list; returns None otherwise
    >>> second_max_num3([10, 4, -1, 7])
    7
    >>> second_max_num3([-5, -2, 0])
    -2
    >>> second_max_num3([1])
    """

    if len(num_list) < 2:
        return

    max_num = num_list[0]

    for num in num_list:
        if num > max_num:
            max_num = num

    num_list.pop(num_list.index(max_num))

    second_max = num_list[0]

    for num in num_list:
        if num > second_max:
            second_max = num

    return second_max


if __name__ == "__main__":
    import doctest
    doctest.testmod()

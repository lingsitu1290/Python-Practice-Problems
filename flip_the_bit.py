# Various ways to return 1 if 0 is given and return 0 if 1 is given 

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    if num == 0:
        return 1
    else:
        return 0

#switch, break, return 

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """
    
    return not num

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    num_dict={0:1,1:0}
    
    return num_dict[num]

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    num_list=[1,0]
    
    return num_list[num]

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    return (num + 1) % 2 

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    return abs(num-1)

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    # ^ Binary XOR  
    # It copies the bit if it is set in one operand but not both. 
    # (a ^ b)

    return (num ^ 1)

def flip_the_bit(num):
    """
    >>> flip_the_bit(1)
    0
    >>> flip_the_bit(0)
    1
    """

    # ^ Binary XOR  
    # It copies the bit if it is set in one operand but not both. 
    # (a ^ b)

    from operator import xor
    return xor(num, 1)

if __name__ == "__main__":
    import doctest
    result = doctest.testmod()
    if result.failed == 0:
        print "ALL TESTS PASSED"
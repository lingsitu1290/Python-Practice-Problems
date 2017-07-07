def substring_in_string(string, substring):
    """
    Returns index of the first occurrence of substring within string
    If substring is not in string, return -1

    >>> substring_in_string('hello world', 'hello')
    0
    >>> substring_in_string('hot potato', 'tao')
    -1
    """

    index = string.find(substring)
    return index

def substring_in_string_v2(string, substring):
    """
    Returns index of the first occurrence of substring within string
    If substring is not in string, return -1

    >>> substring_in_string_v2('hello world', 'hello')
    0
    >>> substring_in_string_v2('hot potato', 'tao')
    -1
    """
    for i in range(len(string)-len(substring)+1):
        # Find the first instance of appearance of the first letter of the substring
    	if string[i] == substring[0]:
            # Initialize the beginning of the substring in string to keep track of length
    		start = 0
    		while start < len(substring) and string[i+start] == substring[start]:
    			start += 1
    		if start == len(substring):
    			return i
    return -1
#########################################################################################

if __name__ == '__main__':
	import doctest
	doctest.testmod()

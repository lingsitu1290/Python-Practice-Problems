"""
Given a nested dictionary. Return a flatten dictionary.
There will be no key collusions.

"""
new_dict ={}

def flatten(nested_dict):
    """
    >>> flatten({1:{1:'like',2:'hello'}, 3:{4:'bye'}, 5:{6:{7:'time'}}})
    {1: 'like', 2: 'hello', 4: 'bye', 7: 'time'}
    >>> flatten({})
    {}
    """
    if nested_dict == {}:
        return {}

    for key in nested_dict:
        if type(nested_dict[key]) is str or type(nested_dict[key]) is int:
            new_dict[key] = nested_dict[key]
        elif type(nested_dict) is dict:
            flatten(nested_dict[key])

    return new_dict

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"

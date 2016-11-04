"""
Input

Your program should expect valid JSON representing a two dimensional matrix. It will be in one of the following two formats:

A) a list of lists

The expected format is [ [variable names], [first row], [second row], ... ]

recombinator '[ ["a","b","c"], [1,2,null], [null,3,4], [5,null,6] ]'
B) a list of objects

JSON objects are simply unordered collections of key:value pairs.

Each row is represented by an object containing the variables set for that row.

Accordingly, this form of input is convenient for sparse data sets.

recombinator '[ { "a":1, "b":2 }, { "b":3, "c":4 }, { "c":6, "a":5 } ]'
Output

Your program should transform the input into a single JSON object mapping variable names to lists of values.

For input type (B), any variables that are missing in a row should be imputed with null.

The order of the values in each variable's list should be the same as the order of the rows.

'{ "a": [1,null,5], "b": [2,3,null], "c": [null,4,6] }'
"""

def transform_to_json(lst_of_lst):
    """
    Given list of list. Transform to JSON object. 

    >>> transform_to_json([["a","b","c"], [1,2,None], [None,3,4], [5,None,6] ])
    '{"a": [1, null, 5], "b": [2, 3, null], "c": [null, 4, 6]}'
    """

    import collections
    import json

    result = collections.OrderedDict()
    
    # zip on multiple lists 
    lst_of_lst = zip(*lst_of_lst)

    for tup in lst_of_lst:
        result[tup[0]] = list(tup[1:])

    return json.dumps(result)

def transform_to_json_2(lst_of_obj):
    """
    Given list of objects. Transform to JSON object. 

    >>> transform_to_json_2([ { "a":1, "b":2 }, { "b":3, "c":4 }, { "c":6, "a":5 } ])
    '{"a": [1, null, 5], "b": [2, 3, null], "c": [null, 4, 6]}'
    """
    import collections 
    import json 

    result = collections.OrderedDict()

    for obj in lst_of_obj:
        for key in obj:
            if key not in result:
                result[key] = []
            else:
                continue

    for obj in lst_of_obj:
        for key in result:
            result[key].append(obj.get(key, None))

    return json.dumps(result)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
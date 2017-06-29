"""
Get all permutations of a given string.

For example, given 'ab' return ab and ba.
Given 'abc', return 'abc','acb','bac','bca','cab','cba'
"""

def permutations(string, prefix=''):
    if len(string) == 0:
        print prefix
    else:
        for i in range(len(string)):
            permutations(string[0:i] + string[i+1:], prefix+string[i])

print permutations('abc')

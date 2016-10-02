"""Return n unique random numbers from 1-10 (inclusive).

Given the numbers 1-10, return `n` random numbers, making sure
to never return the same number twice. You can trust that this
function will never be called with n < 0 or n > 10.

It's tricky to test random functions! However, we can make sure
asking for zero numbers gives us an empty list::

    >>> lucky_numbers(0)
    []

And if we ask for all numbers, we shouldn't get any repeats::

    >>> sorted(lucky_numbers(10))
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""

import random


def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive).

    Time: O(n)
    Space: O(n)
    """

    # Create nums list 
    nums = range(1,11)
    lucky_nums = []

    # Randomly choose a for n iterations and append to lucky_nums list
    for i in range(n):
        num = random.choice(nums)
        nums.remove(num)
        lucky_nums.append(num)

    return sorted(lucky_nums)

def lucky_numbers(n):
    """Return n unique random numbers from 1-10 (inclusive)."""

    # Create nums list 
    nums = range(1,11)
    
    # random.sample(population, k)
    # Return a k length list of unique elements chosen from the 
    # population sequence or set. Used for random sampling 
    # without replacement.
    return random.sample(nums, n)

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT!\n"

"""
Given an unsorted array of non-negative integers, find a continuous subarray which adds to a given number

"""
# Need to optimize 
def subarray_sum_to_target(lst, target):
    """
	>>> subarray_sum_to_target([1, 4, 20, 3, 10, 5], 33)
	[20, 3, 10]
	>>> subarray_sum_to_target([1, 4, 0, 0, 3, 10, 5], 7)
	[4, 0, 0, 3]
	>>> subarray_sum_to_target([1, 4], 0)

    """

    for i in range(len(lst)):
        total = 0
        for j in range(i, len(lst)):
            total += lst[j]
            # print lst[j]
            if total == target:
                return lst[i:j+1]
            if total > target:
                break

    return

if __name__ == '__main__':
	import doctest
	doctest.testmod()

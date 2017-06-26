"""
Cracking the Coding Interview v6: Exercise 16.1
Write a function to swap a number in place (that is, without temporary variables)
"""

def swap_without_temp(num_array, i, j):
	"""
	>>> swap_without_temp([1,2,3,4,5], 0, 3)
	[4, 2, 3, 1, 5]
	>>> swap_without_temp([5,4,3,2,1], 1, 4)
	[5, 1, 3, 2, 4]
	>>> swap_without_temp([4,3,2,6,3], 5, 2)
	"""

	if len(num_array) > i and len(num_array) > j:
		num_array[i], num_array[j] = num_array[j], num_array[i]
		return num_array

	# If i and j is greater than len(num_array) return nothing
	return

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. GREAT JOB!\n"
